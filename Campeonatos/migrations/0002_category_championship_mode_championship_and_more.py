# Generated by Django 4.2.6 on 2023-12-10 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Campeonatos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_championship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(max_length=500, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoria de campeonato',
                'verbose_name_plural': 'Categorias de campeonato',
                'db_table': 'categoria de campeonato',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Mode_championship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(max_length=500, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Modo de campeonato',
                'verbose_name_plural': 'Modos de campeonato',
                'db_table': 'modo de campeonato',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='championship',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campeonatos.category_championship', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='championship',
            name='mode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campeonatos.mode_championship', verbose_name='Modo'),
        ),
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campeonatos.category_championship', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='programming',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campeonatos.category_championship', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='team',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campeonatos.category_championship', verbose_name='Categoría'),
        ),
    ]
