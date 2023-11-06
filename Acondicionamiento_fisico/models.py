from django.db import models

# Aquí se empieza a definir la tabla de Tests
class Test(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    type_test = models.IntegerField(null=False, verbose_name='tipo')
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
        
        
# Aquí se empieza a definir la tabla de Acondicionamiento físico
class Plan(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    category = models.CharField(max_length=30, null=False, verbose_name='Categoría')
    type_plan = models.CharField(max_length=250, null=False, verbose_name='Tipo')
    description = models.CharField(max_length=30, null=False, verbose_name='Descripción')
    category = models.CharField(max_length=30, null=False, verbose_name='Categoría')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Plan'
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'
        ordering = ['id']

  
# Aquí se empieza a definir la tabla de Ejercicios
class Ejercicio(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    description = models.CharField(max_length=250, null=False, verbose_name='Descripción')
    # Pendiente de mirar bien como cargar las imagenes y como organizarlas en carpetas y eso...
    # image = models.ImageField(upload_to='photo/%Y/%m/%d', null=True, blank=True)
    amount = models.IntegerField(null=False, verbose_name='Categoría')
    seconds = models.IntegerField(null=False, verbose_name='Tipo')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'ejercicio'
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'
        ordering = ['id'] 