from datetime import datetime
from django.db import models

# Aquí se empieza a definir la tabla de Entrenamientos
class Type_training(models.Model):

    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tipo de entrenamiento'
        verbose_name = 'Tipo de entrenamiento'
        verbose_name_plural = 'Tipos de entrenamiento'
        ordering = ['id'] 

class Entrenamiento(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    #type_training = models.CharField(max_length=30, null=False, choices=Type_training.name, verbose_name='Tipo de entrenamiento')
    type_training = models.ForeignKey(Type_training, on_delete=models.CASCADE, verbose_name='tipo de entrenamento')        
    description = models.TextField(max_length=500, null=False, verbose_name='Descripción')
    date = models.DateTimeField(default=datetime.now, verbose_name='Fecha de entrenamiento')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'entrenamiento'
        verbose_name = 'Entrenamiento'
        verbose_name_plural = 'Entrenamientos'
        ordering = ['id']