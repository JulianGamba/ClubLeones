from django.contrib import admin
from .models import Entrenamiento

@admin.register(Entrenamiento)
class EntrenamientoAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'type_training')
    #list_display_links = ('name')
    list_editable = ('date',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 2
    