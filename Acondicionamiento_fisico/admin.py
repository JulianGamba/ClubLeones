from django.contrib import admin
from .models import Test, Plan, Ejercicio, Perfil, Type_test, Type_plan
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from sesion_usuario.models import CustomUser

@admin.register(Type_test)
class Type_testAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    #list_display_links = ('name')
    search_fields = ('name', 'description',)
    list_filter = ('description',)
    list_per_page = 5

@admin.register(Type_plan)
class Type_planAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    #list_display_links = ('name')
    search_fields = ('name', 'description',)
    list_filter = ('description',)
    list_per_page = 5

@admin.register(Test)
class TestAdmin(ImportExportModelAdmin):
    list_display = ('name', 'type_test', 'minimum_score', 'maximum_score')
    #list_display_links = ('name')
    #list_editable = ('type_test',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 5

class TestResource(resources.ModelResource):
    class Meta:
        model = Test
        fields = ('name', 'type_test', 'minimum_score', 'maximum_score')
        #export_order = ('name', 'price', 'category')
    
@admin.register(Plan)
class PlanAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category', 'type_plan')
    #list_display_links = ('name')
    #list_editable = ('type_plan',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 5

class PlanResource(resources.ModelResource):
    class Meta:
        model = Plan
        fields = ('name', 'category', 'type_plan')
    
@admin.register(Ejercicio)
class EjercicioAdmin(ImportExportModelAdmin):
    list_display = ('name', 'series_amount', 'amount', 'show_image', 'plan')
    #list_display_links = ('name')
    #list_editable = ('amount',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 5

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
    list_per_page = 5

class PerfilResource(resources.ModelResource):
    class Meta:
        model = Perfil
        fields = ('names', 'last_names', 'email')
