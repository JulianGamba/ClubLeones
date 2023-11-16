from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from ClubLeones.views import *
from .forms import CustomUserCreationForm

#from ClubLeones.views import landingpage

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

# def register_view(request):
#     return render(request,'register.html',{
#         #context
#     })

# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Puedes redirigir a donde quieras después del registro exitoso
#             return redirect('login')  # O a 'dashboard' si deseas después del registro
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'register.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        # Extraer datos del formulario HTML
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Realizar validaciones si es necesario
        
        # Crear el usuario en Django
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        
        # Opcional: iniciar sesión automáticamente después del registro
        login(request, user)
        
        # Redirigir a donde quieras después del registro exitoso
        return redirect('login')  # Cambia 'dashboard' por la URL deseada después del registro
        
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')