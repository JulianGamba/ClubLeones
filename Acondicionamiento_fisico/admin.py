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

# class PerfilAdmin(admin.ModelAdmin):
#     model = Perfil

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'user':
#             # Filtrar los usuarios disponibles para el campo user en el formulario de Perfil
#             kwargs['queryset'] = CustomUser.objects.all()  # Puedes filtrar aquí según tus necesidades

#         return super().formfield_for_foreignkey(db_field, request, **kwargs)

#     def save_model(self, request, obj, form, change):
#         # Verificar si el objeto aún no ha sido guardado y si se ha seleccionado un usuario
#         if not change and obj.user:
#             usuario = obj.user
#             if hasattr(usuario, 'perfil'):
#                 # Si el usuario tiene un perfil, rellenar los campos con los datos del perfil del usuario
#                 obj.names = usuario.perfil.names
#                 obj.last_names = usuario.perfil.last_names
#                 obj.email = usuario.perfil.email
#                 obj.username = usuario.perfil.username
#                 obj.identification = usuario.perfil.identification
#                 obj.age = usuario.perfil.age
#                 obj.resultado_test_velocidad = usuario.perfil.resultado_test_velocidad
#                 obj.resultado_test_fuerza = usuario.perfil.resultado_test_fuerza
#                 obj.resultado_test_resistencia = usuario.perfil.resultado_test_resistencia
#                 obj.resultado_test_flexibilidad = usuario.perfil.resultado_test_flexibilidad
#                 obj.resultado_test_coordinacion = usuario.perfil.resultado_test_coordinacion

#         # Guardar el objeto
#         super().save_model(request, obj, form, change)

# # Registrar el modelo Perfil con el administrador personalizado
# admin.site.register(Perfil, PerfilAdmin)

# class PerfilResource(resources.ModelResource):
#     class Meta:
#         model = Perfil
#         fields = ('names', 'last_names', 'email', 'resultado_test_velocidad', 'resultado_test_fuerza', 'resultado_test_resistencia', 'resultado_test_flexibilidad', 'resultado_test_coordinacion')

# @admin.register(Perfil)
# class PerfilAdmin(ImportExportModelAdmin):
#     model = Perfil
#     resource_class = PerfilResource
#     list_display = ('names', 'last_names', 'email')
#     search_fields = ('names', 'last_names')
#     list_per_page = 5

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'user':
#             kwargs['queryset'] = CustomUser.objects.all()
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)

#     def save_model(self, request, obj, form, change):
#         if not change and obj.user:
#             usuario = obj.user
#             if hasattr(usuario, 'perfil'):
#                 obj.names = usuario.perfil.names
#                 obj.last_names = usuario.perfil.last_names
#                 obj.email = usuario.perfil.email
#                 obj.username = usuario.perfil.username
#                 obj.identification = usuario.perfil.identification
#                 obj.age = usuario.perfil.age
#                 obj.resultado_test_velocidad = usuario.perfil.resultado_test_velocidad
#                 obj.resultado_test_fuerza = usuario.perfil.resultado_test_fuerza
#                 obj.resultado_test_resistencia = usuario.perfil.resultado_test_resistencia
#                 obj.resultado_test_flexibilidad = usuario.perfil.resultado_test_flexibilidad
#                 obj.resultado_test_coordinacion = usuario.perfil.resultado_test_coordinacion

#         super().save_model(request, obj, form, change)

# admin.site.register(Perfil, PerfilAdmin)