from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('admin_dashboard')  # o cambia al destino deseado
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def perfil_view(request):
    user = request.user

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('perfil')  # o el nombre que tengas en urls.py

    context = {
        'user': user
    }
    return render(request, 'users/perfil.html', context)