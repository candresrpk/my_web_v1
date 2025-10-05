from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # crea el usuario automáticamente con password cifrado
            login(request, user)  # inicia sesión
            messages.success(request, f'Registro exitoso. Has iniciado sesión como {user.username}')
            return redirect('carpena:home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Has iniciado sesión como {username}')
                return redirect('carpena:home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
                return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    messages.info(request, 'Por favor, inicia sesión para continuar')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente')
    return redirect('carpena:home')