# Generated by Django 4.2.6 on 2023-12-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campeonatos', '0002_category_championship_mode_championship_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='equipment_1',
            field=models.CharField(max_length=30, verbose_name='Equipo_1'),
        ),
        migrations.AlterField(
            model_name='game',
            name='equipment_2',
            field=models.CharField(max_length=30, verbose_name='Equipo_2'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='programming',
            name='equipment_1',
            field=models.CharField(max_length=30, verbose_name='Equipo_1'),
        ),
        migrations.AlterField(
            model_name='programming',
            name='equipment_2',
            field=models.CharField(max_length=30, verbose_name='Equipo_2'),
        ),
    ]