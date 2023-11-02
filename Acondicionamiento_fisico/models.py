from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    type = models.IntegerField(null=False, verbose_name='tipo')
    minimum_score = models.IntegerField(null=False, verbose_name='Puntaje_mínimo')
    maximum_score = models.IntegerField(null=False, verbose_name='Puntaje_máximo')
    low_minimum_score = models.IntegerField(null=False, verbose_name='Puntaje_mínimo_bajo')
    low_maximum_score = models.IntegerField(null=False, verbose_name='Puntaje_máximo_bajo')
    medium_minimum_score = models.IntegerField(null=False, verbose_name='Puntaje_mínimo_medio')
    medium_maximum_score = models.IntegerField(null=False, verbose_name='Puntaje_máximo_medio')
    high_minimum_score = models.IntegerField(null=False, verbose_name='Puntaje_mínimo_alto')
    high_maximum_score = models.IntegerField(null=False, verbose_name='Puntaje_máximo_alto')
    description = models.CharField(max_length=255, null=False, verbose_name='Descripción')


    def __str__(self):
        return self.name
        # return self.type
        # return sel.minimum_score
    
    class Meta:
        db_table = 'Test'
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'
        ordering = ['id']
        #ordering = ['-id'] # Orden descendente