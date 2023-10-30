"""
URL configuration for ClubLeones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landingpage, name='landingpage'),
    path('landingacond/', views.landingacond, name='landingacond'),
    path('landingentre/', views.landingentre, name='landingentre'),
    path('landingcamp/', views.landingcamp, name='landingcamp'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('error404/', views.error404, name='error404'),
    path('error500/', views.error500, name='error500'),


    path('campeonatos/', views.campeonatos, name='campeonatos'),
    path('crear_campeonatos/', views.crear_campeonatos, name='crear_campeonatos'),
    path('editar_campeonatos/', views.editar_campeonatos, name='editar_campeonatos'),

    path('programacion/', views.programacion, name='programacion'),
    path('crear_programacion/', views.crear_programacion, name='crear_programacion'),
    path('editar_programacion/', views.editar_programacion, name='editar_programacion'),

    path('equipos/', views.equipos, name='equipos'),
    path('crear_equipos/', views.crear_equipos, name='crear_equipos'),
    path('editar_equipos/', views.editar_equipos, name='editar_equipos'),

    path('jugadores/', views.jugadores, name='jugadores'),
    path('crear_jugadores/', views.crear_jugadores, name='crear_jugadores'),
    path('editar_jugadores/', views.editar_jugadores, name='editar_jugadores'),

    
    path('entrenamientos/', views.entrenamientos, name='entrenamientos'),
    path('crear_entrenamientos/', views.crear_entrenamientos, name='crear_entrenamientos'),
    path('editar_entrenamientos/', views.editar_entrenamientos, name='editar_entrenamientos'),


    path('tests/', views.tests, name='tests'),
    path('crear_tests/', views.crear_tests, name='crear_tests'),
    path('editar_tests/', views.editar_tests, name='editar_tests'),

    path('planes/', views.planes, name='planes'),
    path('crear_planes/', views.crear_planes, name='crear_planes'),
    path('editar_planes/', views.editar_planes, name='editar_planes'),

    path('ejercicios/', views.ejercicios, name='ejercicios'),
    path('crear_ejercicios/', views.crear_ejercicios, name='crear_ejercicios'),
    path('editar_ejercicios/', views.editar_ejercicios, name='editar_ejercicios'),

]