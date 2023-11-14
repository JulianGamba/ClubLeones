from django.contrib import admin
from .models import Test, Plan, Ejercicio

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_test', 'minimum_score', 'maximum_score')
    #list_display_links = ('name')
    list_editable = ('type_test',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 2
    
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'type_plan')
    #list_display_links = ('name')
    list_editable = ('type_plan',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 2
    
@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'seconds')
    #list_display_links = ('name')
    list_editable = ('amount',)
    search_fields = ('name',)
    #list_filter = ('category',)
    list_per_page = 2