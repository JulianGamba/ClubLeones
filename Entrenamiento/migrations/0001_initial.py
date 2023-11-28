# Generated by Django 4.2.6 on 2023-11-28 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de entrenamiento')),
                ('type_training', models.CharField(max_length=30, verbose_name='Tipo de entrenamiento')),
                ('description', models.TextField(max_length=500, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Entrenamiento',
                'verbose_name_plural': 'Entrenamientos',
                'db_table': 'entrenamiento',
                'ordering': ['id'],
            },
        ),
    ]
