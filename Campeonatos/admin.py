from django.contrib import admin
from .models import Championship, Team, Player, Programming, Game

@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('name_championship', 'mode', 'category')
    #list_display_links = ('name')
    list_editable = ('category',)
    search_fields = ('name_championship',)
    #list_filter = ('category',)
    list_per_page = 2
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'inscription')
    #list_display_links = ('name')
    list_editable = ('inscription',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 2
    
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'identification', 'dorsal')
    #list_display_links = ('name')
    list_editable = ('dorsal',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 2
    
@admin.register(Programming)
class ProgrammingAdmin(admin.ModelAdmin):
    list_display = ('date', 'category')
    #list_display_links = ('name')
    #list_editable = ('category',)
    search_fields = ('category',)
    #list_filter = ('category',)
    list_per_page = 2
    
    
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'result')
    #list_display_links = ('name')
    #list_editable = ('amount',)
    search_fields = ('category',)
    #list_filter = ('category',)
    list_per_page = 2