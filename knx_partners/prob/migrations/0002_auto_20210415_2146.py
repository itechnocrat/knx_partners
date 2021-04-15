# Generated by Django 3.2 on 2021-04-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prob', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название устройства', max_length=50, verbose_name='Название устройства')),
                ('supply_voltage', models.IntegerField(choices=[(380, 'U380'), (230, 'U230'), (24, 'U24'), (12, 'U12')], default='230', help_text='Введите напряжение питания', verbose_name='Напряжение питания')),
                ('power_consumption', models.IntegerField(help_text='Введите потребляемую мощность', verbose_name='Потребляемая мощность')),
                ('control', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], help_text='Управляемое устройство или нет', verbose_name='Управляемость')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]