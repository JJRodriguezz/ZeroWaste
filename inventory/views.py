from django.shortcuts import render, redirect
from .models import Prenda
from .forms import PrendaForm

def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, 'contacto.html')

def lista_prendas(request):
    prendas = Prenda.objects.filter(disponible=True).order_by('-fecha_agregado')
    return render(request, 'lista_prendas.html', {'prendas': prendas})

# Catálogo por categoría
def catalogo_camisetas(request):
    prendas = Prenda.objects.filter(categoria='Camisetas', estado='Disponible')
    return render(request, 'categorias/camisetas.html', {'prendas': prendas})

def catalogo_pantalones(request):
    prendas = Prenda.objects.filter(categoria='Pantalones', estado='Disponible')
    return render(request, 'categorias/pantalones.html', {'prendas': prendas})

def catalogo_bolsosycarteras(request):
    prendas = Prenda.objects.filter(categoria='Bolsos y carteras', estado='Disponible')
    return render(request, 'categorias/bolsosycarteras.html', {'prendas': prendas})

# Funciones de administración
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def agregar_prenda(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST, request.FILES)
        if form.is_valid():
            prenda = form.save(commit=False)
            prenda.disponible = True
            prenda.save()
            return redirect('admin_dashboard')
    else:
        form = PrendaForm()
    return render(request, 'agregar_prenda.html', {'form': form})

def ver_inventario(request):
    prendas = Prenda.objects.all().order_by('-fecha_agregado')
    return render(request, 'ver_inventario.html', {'prendas': prendas})
