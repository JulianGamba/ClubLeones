# Generated by Django 4.2.6 on 2023-12-10 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Entrenamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(max_length=500, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de entrenamiento',
                'verbose_name_plural': 'Tipos de entrenamiento',
                'db_table': 'tipo de entrenamiento',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='entrenamiento',
            name='type_training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrenamiento.type_training', verbose_name='tipo de entrenamento'),
        ),
    ]
