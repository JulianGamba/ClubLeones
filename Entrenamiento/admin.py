from django.contrib import admin
from .models import Entrenamiento
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(Entrenamiento)
class EntrenamientoAdmin(ImportExportModelAdmin):
    list_display = ('name', 'date', 'type_training')
    #list_display_links = ('name')
    list_editable = ('date',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 2

class EntrenamientoResource(resources.ModelResource):
    class Meta:
        model = Entrenamiento
        fields = ('name', 'date')
        #export_order = ('name', 'price', 'category')