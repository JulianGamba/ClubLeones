# Generated by Django 4.2.6 on 2023-11-02 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('id_championship', models.IntegerField(verbose_name='Id_campeonato')),
                ('name_championship', models.CharField(max_length=30, verbose_name='Nombre_campeonato')),
                ('mode', models.IntegerField(verbose_name='modo')),
                ('category', models.CharField(max_length=30, verbose_name='Categoria')),
                ('address', models.IntegerField(verbose_name='Direccion')),
                ('amount_of_equipments', models.IntegerField(verbose_name='cantidad_de_equipos')),
            ],
            options={
                'verbose_name': 'Campeonato',
                'verbose_name_plural': 'Campeonatos',
                'db_table': 'campeonato',
                'ordering': ['id'],
            },
        ),
    ]
