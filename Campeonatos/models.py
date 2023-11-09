from django.db import models


class Campeonatos(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    id_championship = models.IntegerField(null=False, verbose_name='Id_campeonato')
    name_championship = models.IntegerField(max_length=30, null=False, verbose_name='Nombre_campeonato')
    mode = models.IntegerField(null=False, verbose_name='Modo')
    category = models.IntegerField(max_length=30, null=False, verbose_name='Categoria')
    address = models.IntegerField(null=False, verbose_name='Direccion')
    amount_of_equipments = models.IntegerField(null=False, verbose_name='cantidad_de_equipos')
  

    def __str__(self):
        return self.name
        # return self.type
        # return sel.minimum_score
    
    class Meta:
        db_table = 'campeonato'
        verbose_name = 'Campeonato'
        verbose_name_plural = 'Campeonatos'
        ordering = ['id']
        #ordering = ['-id'] # Orden descendente
        
        
# Aquí se empieza a definir la tabla de Acondicionamiento físico
class Equipo(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    id_equipments = models.CharField(null=False, verbose_name='Id_equipos')
    category = models.CharField(max_length=30, null=False, verbose_name='Categoría')
    inscription = models.CharField(null=False, verbose_name='Inscripcion')
    equipement = models.CharField(null=False, verbose_name='Equipacion')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'equipo'
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['id']

  

class Jugador(models.Model):
    id_player = models.CharField(null=False, verbose_name='Id_jugador')
    id_equipment = models.CharField(null=False, verbose_name='Id_equipo')
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    identification = models.CharField(null=False, verbose_name='Identificacion')
    dorsal = models.IntegerField(null=False, verbose_name='Dorsal')
    age = models.IntegerField(null=False, verbose_name='Edad')
    contact_number = models.IntegerField(null=False, verbose_name='Numero de contacto')


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'jugador'
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering = ['id'] 



class Programacion(models.Model):
    day = models.CharField(null=False, verbose_name='dia')
    hour = models.CharField(null=False, verbose_name='hora')
    category = models.CharField(max_length=30, null=False, verbose_name='Categoría')
    equipment_1 = models.CharField(max_length=30, null=False, unique=True, verbose_name='Equipo_1')
    equipment_2 = models.CharField(max_length=30, null=False, unique=True, verbose_name='Equipo_2')
    address = models.IntegerField(null=False, verbose_name='Direccion')


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'programacion'
        verbose_name = 'Programacion'
        verbose_name_plural = 'Programaciones'
        ordering = ['id'] 