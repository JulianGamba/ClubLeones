from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from ClubLeones.views import *

from sesion_usuario.models import CustomUser

#Aquí empiezan las rutas del login y el register

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('dashboard')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })

def register_view(request):
    if request.method == 'POST':

        # Extraer datos del formulario HTML
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        identification = request.POST.get('identification')
        age = request.POST.get('age')
        cellphone_number = request.POST.get('cellphone_number')
        email = request.POST.get('email')
        username = request.POST.get('username')

        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        # Realizar validaciones si es necesario

        # Realiza la validación de las contraseñas
        if password == password1:
            # Si las contraseñas coinciden, crea el usuario
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                age=age,
                identification=identification,
                cellphone_number=cellphone_number
            )
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect('login')  # Redirige a la página deseada después del registro exitoso
        else:
            # Si las contraseñas no coinciden, maneja la situación
            # Por ejemplo, puedes añadir un error al campo 'password1'
            error_message = "Las contraseñas no coinciden"
            return render(request, 'register.html', {'error_message': error_message})        

    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')