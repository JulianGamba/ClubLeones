from django.db import models
from django.utils.html import format_html
from sesion_usuario.models import CustomUser

# Aquí se empieza a definir la tabla de Tests
class Type_test(models.Model):

    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tipo de test'
        verbose_name = 'Tipo de test'
        verbose_name_plural = 'Tipos de test'
        ordering = ['id'] 

class Test(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    #type_test = models.IntegerField(null=False, choices=Type_test.name,  verbose_name='tipo')
    type_test = models.ForeignKey(Type_test, on_delete=models.CASCADE, verbose_name='tipo')    
    minimum_score = models.IntegerField(null=False, verbose_name='Puntaje_mínimo')
    maximum_score = models.IntegerField(null=False, verbose_name='Puntaje_máximo')
    low_minimum_score = models.IntegerField(null=False, verbose_name='Puntaje_mínimo_bajo')
    low_maximum_score = models.IntegerField(null=False, verbose_name='Puntaje_máximo_bajo')
    medium_minimum_score = models.IntegerField(null=False, verbose_name='Puntaje_mínimo_medio')
    medium_maximum_score = models.IntegerField(null=False, verbose_name='Puntaje_máximo_medio')
    high_minimum_score = models.IntegerField(null=False, verbose_name='Puntaje_mínimo_alto')
    high_maximum_score = models.IntegerField(null=False, verbose_name='Puntaje_máximo_alto')
    description = models.TextField(max_length=500, null=False, verbose_name='Descripción')

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

# Aquí se empieza a definir la tabla de Planes de acondicionamiento físico
class Type_plan(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tipo de plan'
        verbose_name = 'Tipo de plan'
        verbose_name_plural = 'Tipos de plan'
        ordering = ['id']        
        
# Aquí se empieza a definir la tabla de Planes de acondicionamiento físico
class Plan(models.Model):

    categorias = (
        ('bajo', 'Bajo'),
        ('medio', 'Medio'),
        ('alto', 'Alto'),
    )

    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    category = models.CharField(max_length=30, null=False, choices=categorias,  verbose_name='Categoría')
    #type_plan = models.CharField(max_length=250, null=False, choices=Type_plan.name,  verbose_name='Tipo')
    type_plan = models.ForeignKey(Type_plan, on_delete=models.CASCADE, verbose_name='tipo')    
    description = models.TextField(max_length=500, null=False, verbose_name='Descripción')

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
    description = models.TextField(max_length=500, null=False, verbose_name='Descripción')
    image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='imagen del ejercicio')
    series_amount = models.IntegerField(null=False, verbose_name='Cantidad de series')
    amount = models.IntegerField(null=False, verbose_name='Cantidad')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def show_image(self):
        return format_html('<img src={} width="100" /> ', self.image.url)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ejercicio'
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'
        ordering = ['id']  

# Aquí se empieza a definir la tabla de Ejercicios
class Perfil(models.Model):
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='perfil')    
    names = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombres')
    last_names = models.CharField(max_length=30, null=False, unique=True, verbose_name='Apellidos')
    email = models.TextField(max_length=500, null=False, verbose_name='Correo')
    username = models.CharField(max_length=30, null=False, verbose_name='Nombre de usuario')
    identification = models.IntegerField(null=False, verbose_name='Identificación')
    age = models.IntegerField(null=False, verbose_name='Edad')

    resultado_test_velocidad = models.CharField(max_length=100, blank=True, null=True)
    resultado_test_fuerza = models.CharField(max_length=100, blank=True, null=True) 
    resultado_test_resistencia = models.CharField(max_length=100, blank=True, null=True) 
    resultado_test_flexibilidad = models.CharField(max_length=100, blank=True, null=True) 
    resultado_test_coordinacion = models.CharField(max_length=100, blank=True, null=True) 

    def __str__(self):
        return self.names
    
    class Meta:
        db_table = 'Perfil'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['id']  


#En el registro se debe pedir los siguientes datos:
# nombres, apellidos, correo, usuario, contraseña, confirmar contraseña, identificacion
# edad del jugador