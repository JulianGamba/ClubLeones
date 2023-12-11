from datetime import datetime
from django.db import models

class Mode_championship(models.Model):

    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'modo de campeonato'
        verbose_name = 'Modo de campeonato'
        verbose_name_plural = 'Modos de campeonato'
        ordering = ['id'] 

class Category_championship(models.Model):

    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categoria de campeonato'
        verbose_name = 'Categoria de campeonato'
        verbose_name_plural = 'Categorias de campeonato'
        ordering = ['id'] 

class Championship(models.Model):
    name_championship = models.CharField(max_length=30, null=False, verbose_name='Nombre_campeonato')
    #mode = models.CharField(null=False, choices=Mode_championship.name, verbose_name='Modo')
    mode = models.ForeignKey(Mode_championship, on_delete=models.CASCADE, verbose_name='Modo')
    #category = models.CharField(null=False, choices=Category_championship.name, verbose_name='Categoria')
    category = models.ForeignKey(Category_championship, on_delete=models.CASCADE, verbose_name='Categoría')
    address = models.CharField(max_length=30, null=False, verbose_name='Direccion')
    amount_of_equipments = models.IntegerField(null=False, verbose_name='cantidad_de_equipos')
  

    def __str__(self):
        return self.name_championship
        # return self.type
        # return sel.minimum_score
    
    class Meta:
        db_table = 'campeonato'
        verbose_name = 'Campeonato'
        verbose_name_plural = 'Campeonatos'
        ordering = ['id']
        #ordering = ['-id'] # Orden descendente
        
        
# Aquí se empieza a definir la tabla de Acondicionamiento físico
class Team(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True, verbose_name='Nombre')
    #category = models.CharField(max_length=30, null=False, choices=Category_championship.name, verbose_name='Categoría')
    category = models.ForeignKey(Category_championship, on_delete=models.CASCADE, verbose_name='Categoría')
    inscription = models.CharField(max_length=30, null=False, verbose_name='Inscripcion')
    color_equipment = models.CharField(max_length=30, null=False, verbose_name='Color_equipacion')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'equipo'
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['id']

  

class Player(models.Model):
    name = models.CharField(max_length=30, null=False, verbose_name='Nombre')
    identification = models.IntegerField(null=False, verbose_name='Identificacion')
    dorsal = models.IntegerField(null=False, verbose_name='Dorsal')
    age = models.IntegerField(null=False, verbose_name='Edad')
    contact_number = models.IntegerField(null=False, verbose_name='Numero de contacto')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'jugador'
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering = ['id'] 



class Programming(models.Model):
    #hour = models.CharField(null=False, verbose_name='hora')
    #category = models.CharField(max_length=30, null=False, choices=Category_championship.name, verbose_name='Categoría')
    category = models.ForeignKey(Category_championship, on_delete=models.CASCADE, verbose_name='Categoría')    
    equipment_1 = models.CharField(max_length=30, null=False, verbose_name='Equipo_1')
    equipment_2 = models.CharField(max_length=30, null=False, verbose_name='Equipo_2')
    address = models.CharField(max_length=30, null=False, verbose_name='Direccion')
    date = models.DateTimeField(null=False, verbose_name='fecha')


    def __str__(self):
        return self.equipment_1
    
    class Meta:
        db_table = 'programación'
        verbose_name = 'Programación'
        verbose_name_plural = 'Programaciones'
        ordering = ['id'] 
        

class Game(models.Model):
    #category = models.CharField(max_length=30, null=False, choices=Category_championship.name, verbose_name='Categoría')
    category = models.ForeignKey(Category_championship, on_delete=models.CASCADE, verbose_name='Categoría')    
    equipment_1 = models.CharField(max_length=30, null=False, verbose_name='Equipo_1')
    equipment_2 = models.CharField(max_length=30, null=False, verbose_name='Equipo_2')
    team_goals1 = models.IntegerField(null=True, verbose_name='Goles Equipo 1')
    player_frame_goal_team1 = models.CharField(max_length=30, null=True, verbose_name='Jugador que marcó Gol Equipo 1')
    team_goals2 = models.IntegerField(null=True, verbose_name='Goles Equipo 2')
    player_frame_goal_team2 = models.CharField(max_length=30, null=True, verbose_name='Jugador que marcó Gol Equipo 2')
    result = models.CharField(max_length=30, null=True, verbose_name='Resultado')
    fouls_committed_team1 = models.IntegerField(null=True, verbose_name='Faltas Cometidas Equipo 1')
    fouls_committed_team2 = models.IntegerField(null=True, verbose_name='Faltas Cometidas Equipo 2')
    yellow_cards_team1 = models.IntegerField(null=True, verbose_name='Tarjetas Amarillas Equipo 1')
    yellow_cards_team2 = models.IntegerField(null=True, verbose_name='Tarjetas Amarillas Equipo 2')
    red_cards_team1 = models.IntegerField(null=True, verbose_name='Tarjetas Rojas Equipo 1')
    red_cards_team2 = models.IntegerField(null=True, verbose_name='Tarjetas Rojas Equipo 2')
    #payment_arbitration_team1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='Pago Arbitraje Equipo 1')
    payment_arbitration_team1 = models.CharField(max_length=30, null=True, verbose_name='Pago Arbitraje Equipo 1')
    #payment_arbitration_team2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='Pago Arbitraje Equipo 2')
    payment_arbitration_team2 = models.CharField(max_length=30, null=True, verbose_name='Pago Arbitraje Equipo 2')
    date = models.DateTimeField(null=False, verbose_name='fecha')
    programming = models.ForeignKey(Programming, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.equipment_1} vs {self.equipment_2} ({self.date.strftime("%Y-%m-%d %H:%M")})'

    class Meta:
        db_table = 'partido'
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'
        ordering = ['id']