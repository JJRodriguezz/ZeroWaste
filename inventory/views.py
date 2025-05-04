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