from django.shortcuts import render, redirect
from .models import Prenda
from .forms import PrendaForm
# Create your views here.

def lista_prendas(request):
    prendas = Prenda.objects.filter(disponible=True).order_by('-fecha_agregado')
    return render(request, 'lista_prendas.html', {'prendas': prendas})


def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, 'contacto.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def agregar_prenda(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST, request.FILES)
        if form.is_valid():
            prenda = form.save(commit=False)
            prenda.disponible = True  # siempre disponible al registrarla
            prenda.save()
            return redirect('admin_dashboard')
    else:
        form = PrendaForm()
    return render(request, 'agregar_prenda.html', {'form': form})