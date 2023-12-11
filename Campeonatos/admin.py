from django.contrib import admin
from .models import Championship, Team, Player, Programming, Game, Mode_championship, Category_championship

@admin.register(Mode_championship)
class Mode_championshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    #list_display_links = ('name')
    search_fields = ('name', 'description',)
    list_filter = ('description',)
    list_per_page = 5

@admin.register(Category_championship)
class Mode_championshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    #list_display_links = ('name')
    search_fields = ('name', 'description',)
    list_filter = ('description',)
    list_per_page = 5

@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('name_championship', 'mode', 'category', 'address', 'amount_of_equipments')
    #list_display_links = ('name')
    #list_editable = ('category',)
    search_fields = ('name_championship',)
    #list_filter = ('category',)
    list_per_page = 5
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'inscription', 'color_equipment')
    #list_display_links = ('name')
    #list_editable = ('inscription',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 5
    
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'identification', 'dorsal', 'age', 'contact_number', 'team')
    #list_display_links = ('name')
    #list_editable = ('dorsal',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 5
    
@admin.register(Programming)
class ProgrammingAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'equipment_1', 'equipment_2')
    #list_display_links = ('name')
    #list_editable = ('category',)
    search_fields = ('category',)
    #list_filter = ('category',)
    list_per_page = 5
    
    
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'equipment_1', 'equipment_2', 'result')
    #list_display_links = ('name')
    #list_editable = ('amount',)
    search_fields = ('category',)
    #list_filter = ('category',)
    list_per_page = 5