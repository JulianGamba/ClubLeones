# Generated by Django 4.2.6 on 2023-12-10 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campeonatos', '0003_alter_game_equipment_1_alter_game_equipment_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='payment_arbitration_team1',
            field=models.CharField(max_length=30, null=True, verbose_name='Pago Arbitraje Equipo 1'),
        ),
        migrations.AlterField(
            model_name='game',
            name='payment_arbitration_team2',
            field=models.CharField(max_length=30, null=True, verbose_name='Pago Arbitraje Equipo 2'),
        ),
    ]
