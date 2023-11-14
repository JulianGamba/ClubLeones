from datetime import datetime
from django.db import models

# Aquí se empieza a definir la tabla de Entrenamientos
class Entrenamiento(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    date = models.DateTimeField(default=datetime.now, verbose_name='Fecha de entrenamiento')
    type_training = models.CharField(max_length=30, null=False, verbose_name='Tipo de entrenamiento')
    description = models.TextField(max_length=500, null=False, verbose_name='Descripción')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'entrenamiento'
        verbose_name = 'Entrenamiento'
        verbose_name_plural = 'Entrenamientos'
        ordering = ['id']