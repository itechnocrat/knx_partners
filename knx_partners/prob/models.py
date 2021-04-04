from django.db import models


class ProbChoice(models.Model):
    HOUSE = 'house'  # частный дом
    APARTMENT = 'apartment'  # квартира
    STOCK = 'stock'  # склад
    THE_CHOICE = [
        (HOUSE, 'Частный дом'),
        (APARTMENT, 'Квартира'),
        (STOCK, 'Склад')
    ]


class ProbRadioSelect(models.Model):
    THE_CHOICE = [('select1', 'Потолочная люстра'),
                  ('select2', 'Поджопный светильник')]
