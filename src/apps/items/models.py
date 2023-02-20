from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='')

    class Meta:
        db_table = 'items'


class ItemPrice(models.Model):
    class Currencies(models.TextChoices):
        RUB = 'rub'
        USD = 'usd'

    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=3, choices=Currencies.choices)

    class Meta:
        db_table = 'item_prices'
