from django.http import HttpResponse
from django.shortcuts import render

# Aquí van las rutas de la landing page

def landingpage(request):
    return render(request,'landingpage.html',{
        #context
    })

def landingcamp(request):
    return render(request,'landingcamp.html',{
        #context
    })

def landingacond(request):
    return render(request,'landingacond.html',{
        #context
    })

def landingentre(request):
    return render(request,'landingentre.html',{
        #context
    })

#Aquí empiezan las rutas del login y el register

def login(request):
    return render(request,'login.html',{
        #context
    })

def register(request):
    return render(request,'register.html',{
        #context
    })

# Aquí está la ruta del dashboard

def dashboard(request):
    return render(request,'dashboard.html',{
        #context
    })

# Aquí está la ruta de los errores

def error404(request):
    return render(request,'error404.html',{
        #context
    })

def error500(request):
    return render(request,'error500.html',{
        #context
    })

# Aquí empiezan las rutas del módulo de campeonatos
# Aquí están las rutas de campeonatos

def campeonatos(request):
    return render(request,'campeonatos/campeonatos.html',{
        #context
    })

def crear_campeonatos(request):
    return render(request,'campeonatos/crear_campeonatos.html',{
        #context
    })

def editar_campeonatos(request):
    return render(request,'campeonatos/editar_campeonatos.html',{
        #context
    })

# Aquí están las rutas de equipos

def equipos(request):
    return render(request,'campeonatos/equipos.html',{
        #context
    })

def crear_equipos(request):
    return render(request,'campeonatos/crear_equipos.html',{
        #context
    })

def editar_equipos(request):
    return render(request,'campeonatos/editar_equipos.html',{
        #context
    })

# Aquí están las rutas de jugadores

def jugadores(request):
    return render(request,'campeonatos/jugadores.html',{
        #context
    })

def crear_jugadores(request):
    return render(request,'campeonatos/crear_jugadores.html',{
        #context
    })

def editar_jugadores(request):
    return render(request,'campeonatos/editar_jugadores.html',{
        #context
    })

# Aquí están las rutas de programación

def programacion(request):
    return render(request,'campeonatos/programacion.html',{
        #context
    })

def crear_programacion(request):
    return render(request,'campeonatos/crear_programacion.html',{
        #context
    })

def editar_programacion(request):
    return render(request,'campeonatos/editar_programacion.html',{
        #context
    })

# Aquí empiezan las rutas del módulo de entrenamientos

def entrenamientos(request):
    return render(request,'entrenamientos/entrenamientos.html',{
        #context
    })

def crear_entrenamientos(request):
    return render(request,'entrenamientos/crear_entrenamientos.html',{
        #context
    })

def editar_entrenamientos(request):
    return render(request,'entrenamientos/editar_entrenamientos.html',{
        #context
    })

# Aquí empiezan las rutas del módulo de acondicionamiento físico
# Aquí están las rutas de tests

def tests(request):
    return render(request,'acondicionamiento_fisico/tests.html',{
        #context
    })

def crear_tests(request):
    return render(request,'acondicionamiento_fisico/crear_tests.html',{
        #context
    })

def editar_tests(request):
    return render(request,'acondicionamiento_fisico/editar_tests.html',{
        #context
    })

# Aquí están las rutas de planes

def planes(request):
    return render(request,'acondicionamiento_fisico/planes.html',{
        #context
    })

def crear_planes(request):
    return render(request,'acondicionamiento_fisico/crear_planes.html',{
        #context
    })

def editar_planes(request):
    return render(request,'acondicionamiento_fisico/editar_planes.html',{
        #context
    })

# Aquí están las rutas de ejercicios

def ejercicios(request):
    return render(request,'acondicionamiento_fisico/ejercicios.html',{
        #context
    })

def crear_ejercicios(request):
    return render(request,'acondicionamiento_fisico/crear_ejercicios.html',{
        #context
    })

def editar_ejercicios(request):
    return render(request,'acondicionamiento_fisico/editar_ejercicios.html',{
        #context
    })