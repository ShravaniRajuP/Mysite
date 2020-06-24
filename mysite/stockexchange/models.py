from django.db import models


# Create your models here.


class Player(models.Model):
    player_name = models.CharField(max_length=200)
    player_starting_amount = models.IntegerField(default=600000)
    player_cards = []

    def __str__(self):
        return self.player_name


class Cards(models.Model):
    card_company = models.CharField(max_length=20)
    card_value = models.IntegerField(default=0)
    card_player = models.ForeignKey(Player, on_delete=models.CASCADE)


class Company(models.Model):
    company_name = models.CharField(max_length=20)
    company_starting_price = models.IntegerField(default=0)
    company_current_price = models.IntegerField(default=0)
    company_total_shares = models.IntegerField(default=200000)
    company_remaining_shares = models.IntegerField(default=200000)

    def __str__(self):
        return self.company_name




