from django.contrib import admin
from .models import Test, Plan, Ejercicio, Perfil
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(Test)
class TestAdmin(ImportExportModelAdmin):
    list_display = ('name', 'type_test', 'minimum_score', 'maximum_score')
    #list_display_links = ('name')
    list_editable = ('type_test',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 2

class TestResource(resources.ModelResource):
    class Meta:
        model = Test
        fields = ('name', 'type_test', 'minimum_score', 'maximum_score')
        #export_order = ('name', 'price', 'category')
    
@admin.register(Plan)
class PlanAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category', 'type_plan')
    #list_display_links = ('name')
    list_editable = ('type_plan',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 2

class PlanResource(resources.ModelResource):
    class Meta:
        model = Plan
        fields = ('name', 'category', 'type_plan')
    
@admin.register(Ejercicio)
class EjercicioAdmin(ImportExportModelAdmin):
    list_display = ('name', 'series_amount', 'amount', 'show_image', 'plan')
    #list_display_links = ('name')
    list_editable = ('amount',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 2

class EjercicioResource(resources.ModelResource):
    class Meta:
        model = Ejercicio
        fields = ('name', 'series_amount', 'amount', 'show_image', 'plan')

@admin.register(Perfil)
class PerfilAdmin(ImportExportModelAdmin):
    list_display = ('names', 'last_names', 'email')
    #list_display_links = ('name')
    #list_editable = ('amount',)
    search_fields = ('names', 'last_names')
    #list_filter = ('category',)
    list_per_page = 2

class PerfilResource(resources.ModelResource):
    class Meta:
        model = Perfil
        fields = ('names', 'last_names', 'email')