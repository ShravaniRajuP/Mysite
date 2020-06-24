from django.http import HttpResponse
from django.shortcuts import render
from .models import Player, Cards, Company
import random

# Create your views here.

list_of_companies = {'Wockhardt': 20, 'HDFC': 25, 'TATA': 40, 'ONGC': 55, 'Reliance': 75, 'Infosys': 80}


def index(request):
    return render(request, 'stockexchange/index.html')


def create_company():

    price_range = [-30, -30, 30, 30, -25, -25, 25, 25, -20, -20, 20, 20,
                   -15, -15, 15, 15, -10, -10, 10, 10, -5, -5, 5, 5]

    list_cards = []
    company_range = [8, 12, 12, 16, 20, 24]
    i = 0
    for company in list_of_companies.keys():

        current_number = company_range[i]
        a = -current_number
        for value in price_range[a:]:
            temp = Cards(card_company=company, card_value=value)
            list_cards.append(temp)
        i += 1

    return list_cards


def assign_cards(list_cards, player_list):
    for player in player_list:
        random.shuffle(list_cards)
        player.player_cards = sorted(list_cards[:10],key=lambda x: x.card_company)
        list_cards = list_cards[10:]



def player_initiate(name):
    player = player = Player(player_name=name)
    return player


def game(request):
    player_number = request.POST.get('player_numbers', None)
    list_cards = create_company()
    list_of_players = []
    for i in range(int(player_number)):
        player = player_initiate("player{}".format(i))
        list_of_players.append(player)

    assign_cards(list_cards, list_of_players)
    return render(request, 'stockexchange/game.html', {'players': list_of_players,
                                                       'company_list': list_of_companies})


def buy(request):
    return render(request, 'stockexchange/game.html', {'players': list_of_players,
                                                       'company_list': list_of_companies})


def sell(request):
    return HttpResponse("This button is used to sell shares")


def pass_turn(request):
    return HttpResponse("This button is used to pass your turn")
