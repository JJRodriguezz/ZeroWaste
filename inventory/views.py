from django.shortcuts import render, redirect
from .models import Prenda
from .forms import PrendaForm
import unicodedata
from inventory.models import Subcategoria


def normalizar(texto):
    if not texto:
        return ''
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8').lower()

def lista_prendas(request):
    query = request.GET.get('q', '').strip()
    prendas = Prenda.objects.filter(disponible=True)

    if query:
        query_norm = normalizar(query)

        if len(query) == 1:
            prendas = prendas.filter(talla__iexact=query)
        else:
            prendas = [prenda for prenda in prendas if 
                       query_norm in normalizar(prenda.nombre) or
                       query_norm in normalizar(prenda.descripcion)]

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
            prenda.disponible = True  # Siempre disponible al registrarla
            prenda.save()
            return redirect('admin_dashboard')
    else:
        form = PrendaForm()
    
    subcategorias = Subcategoria.objects.select_related('categoria')
    
    return render(request, 'agregar_prenda.html', {
        'form': form,
        'subcategorias': subcategorias
    })

def ver_inventario(request):
    prendas = Prenda.objects.all().order_by('-fecha_agregado')
    return render(request, 'ver_inventario.html', {'prendas': prendas})