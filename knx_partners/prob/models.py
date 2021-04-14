from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField


# class ProbChoice(models.Model):
#     HOUSE = 'house'  # частный дом
#     APARTMENT = 'apartment'  # квартира
#     STOCK = 'stock'  # склад
#     THE_CHOICE = [
#         (HOUSE, 'Частный дом'),
#         (APARTMENT, 'Квартира'),
#         (STOCK, 'Склад')
#     ]


# class ProbRadioSelect(models.Model):
#     THE_CHOICE = [('select1', 'Потолочная люстра'),
#                   ('select2', 'Поджопный светильник')]


# class Object_Of_Lighting(models.Model):
#     number_of_zone = models.

class Device(models.Model):

    class ChoiceVoltage(models.IntegerChoices):
        U380 = 380
        U230 = 230
        U24 = 24
        U12 = 12

    class ChoiceControl(models.IntegerChoices):
        No = 0
        Yes = 1
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        max_length=50, help_text='Введите название устройства', verbose_name='Название устройства')
    supply_voltage = models.IntegerField(
        choices=ChoiceVoltage.choices, default='230', help_text='Введите напряжение питания', verbose_name='Напряжение питания')
    power_consumption = models.IntegerField(
        help_text='Введите потребляемую мощность', verbose_name='Потребляемая мощность')
    control = models.IntegerField(choices=ChoiceControl.choices,
                                  help_text='Управляемое устройство или нет', verbose_name='Управляемость')
