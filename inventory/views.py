from django.shortcuts import render
from .models import Prenda
# Create your views here.

def lista_prendas(request):
    prendas = Prenda.objects.filter(disponible=True).order_by('-fecha_agregado')
    return render(request, 'lista_prendas.html', {'prendas': prendas})


def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, 'contacto.html')

def catalogo_camisetas(request):
    prendas = Prenda.objects.filter(categoria='Camisetas', estado='Disponible')
    return render(request, 'categorias/camisetas.html', {
        'prendas': prendas
    })
def catalogo_pantalones(request):
    prendas = Prenda.objects.filter(categoria='Pantalones', estado='Disponible')
    return render(request, 'categorias/pantalones.html', {'prendas': prendas})
def catalogo_bolsosycarteras(request):
    prendas = Prenda.objects.filter(categoria='Bolsos y carteras', estado='Disponible')
    return render(request, 'categorias/bolsosycarteras.html', {'prendas': prendas})
