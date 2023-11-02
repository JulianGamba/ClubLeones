# Generated by Django 4.2.6 on 2023-11-02 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('type', models.IntegerField(verbose_name='tipo')),
                ('minimum_score', models.IntegerField(verbose_name='Puntaje_mínimo')),
                ('maximum_score', models.IntegerField(verbose_name='Puntaje_máximo')),
                ('low_minimum_score', models.IntegerField(verbose_name='Puntaje_mínimo_bajo')),
                ('low_maximum_score', models.IntegerField(verbose_name='Puntaje_máximo_bajo')),
                ('medium_minimum_score', models.IntegerField(verbose_name='Puntaje_mínimo_medio')),
                ('medium_maximum_score', models.IntegerField(verbose_name='Puntaje_máximo_medio')),
                ('high_minimum_score', models.IntegerField(verbose_name='Puntaje_mínimo_alto')),
                ('high_maximum_score', models.IntegerField(verbose_name='Puntaje_máximo_alto')),
                ('description', models.CharField(max_length=255, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
                'db_table': 'Test',
                'ordering': ['id'],
            },
        ),
    ]