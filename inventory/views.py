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

#catalogoooo
def catalogo_bebebodies(request):
    prendas = Prenda.objects.filter(
        subcategoria__nombre='Bodies',
        subcategoria__categoria__grupo__nombre='Bebé',
        disponible=True
    )
    return render(request, 'categorias/Bebe/BebeBodies.html', {'prendas': prendas})
def catalogo_bebeconjuntos(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Conjuntos',
       subcategoria__categoria__grupo__nombre='Bebé',
       disponible=True
   )
   return render(request, 'categorias/Bebe/BebeConjuntos.html', {'prendas': prendas})
def catalogo_bebepijamas(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Pijamas',
       subcategoria__categoria__grupo__nombre='Bebé',
       disponible=True
   )
   return render(request, 'categorias/Bebe/BebePijamas.html', {'prendas': prendas})
def catalogo_niñocamisas(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Camisas',
       subcategoria__categoria__grupo__nombre='Niño',
       disponible=True
   )
   return render(request, 'categorias/Niño/NiñoCamisas.html', {'prendas': prendas})
def catalogo_niñochaquetas(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Chaquetas',
       subcategoria__categoria__grupo__nombre='Niño',
       disponible=True
   )
   return render(request, 'categorias/Niño/NiñoChaquetas.html', {'prendas': prendas})
def catalogo_niñopantalones(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Pantalones',
       subcategoria__categoria__grupo__nombre='Niño',
       disponible=True
   )
   return render(request, 'categorias/Niño/NiñoPantalones.html', {'prendas': prendas})
def catalogo_niñozapatos(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Zapatos',
       subcategoria__categoria__grupo__nombre='Niño',
       disponible=True
   )
   return render(request, 'categorias/Niño/NiñoZapatos.html', {'prendas': prendas})
def catalogo_hombrecamisas(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Camisas',
       subcategoria__categoria__grupo__nombre='Hombre',
       disponible=True
   )
   return render(request, 'categorias/Hombre/HombreCamisas.html', {'prendas': prendas})
def catalogo_hombrechaquetas(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Chaquetas',
       subcategoria__categoria__grupo__nombre='Hombre',
       disponible=True
   )
   return render(request, 'categorias/Hombre/HombreChaquetas.html', {'prendas': prendas})
def catalogo_hombrepantalones(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Pantalones',
       subcategoria__categoria__grupo__nombre='Hombre',
       disponible=True
   )
   return render(request, 'categorias/Hombre/HombrePantalones.html', {'prendas': prendas})
def catalogo_hombrezapatos(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Zapatos',
       subcategoria__categoria__grupo__nombre='Hombre',
       disponible=True
   )
   return render(request, 'categorias/Hombre/HombreZapatos.html', {'prendas': prendas})
def catalogo_hombredeportivos(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Deportivos',
       subcategoria__categoria__grupo__nombre='Hombre',
       disponible=True
   )
   return render(request, 'categorias/Hombre/HombreDeportivos.html', {'prendas': prendas})
def catalogo_hombreblazers(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Blazers',
       subcategoria__categoria__grupo__nombre='Hombre',
       disponible=True
   )
   return render(request, 'categorias/Hombre/HombreBlazers.html', {'prendas': prendas})
def catalogo_mujerbolsos(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Bolsos',
       subcategoria__categoria__grupo__nombre='MujerAccesorios',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Accesorios(Mujer)/MujerBolsos.html', {'prendas': prendas})
def catalogo_mujerzapatos(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Zapatos',
       subcategoria__categoria__grupo__nombre='MujerAccesorios',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Accesorios(Mujer)/MujerZapatos.html', {'prendas': prendas})
def catalogo_mujersandalias(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Bolsos',
       subcategoria__categoria__grupo__nombre='MujerSandalias',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Accesorios(Mujer)/MujerSandalias.html', {'prendas': prendas})
def catalogo_mujeraccesorios(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Accesorios',
       subcategoria__categoria__grupo__nombre='MujerAccesorios',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Accesorios(Mujer)/MujerAccesorios.html', {'prendas': prendas})
def catalogo_mujerropainterior(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='RopaInterior',
       subcategoria__categoria__grupo__nombre='MujerEspeciales',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Especiales(Mujer)/MujerRopaInterior.html', {'prendas': prendas})
def catalogo_mujerpijamas(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Pijamas',
       subcategoria__categoria__grupo__nombre='MujerEspeciales',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Especiales(Mujer)/MujerPijamas.html', {'prendas': prendas})
def catalogo_mujerdeportivos(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Deportivos',
       subcategoria__categoria__grupo__nombre='MujerEspeciales',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Especiales(Mujer)/MujerDeportivos.html', {'prendas': prendas})
def catalogo_mujerconjuntos(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Conjuntos',
       subcategoria__categoria__grupo__nombre='MujerEspeciales',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Especiales(Mujer)/MujerConjuntos.html', {'prendas': prendas})
def catalogo_mujertrajesdebaño(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='TrajesDeBaño',
       subcategoria__categoria__grupo__nombre='MujerEspeciales',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Especiales(Mujer)/MujerTrajesDeBaño.html', {'prendas': prendas})
def catalogo_mujerbodies(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Bodies',
       subcategoria__categoria__grupo__nombre='MujerInferior',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Inferior(Mujer)/MujerBodies.html', {'prendas': prendas})
def catalogo_mujershorts(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Shorts',
       subcategoria__categoria__grupo__nombre='MujerInferior',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Inferior(Mujer)/MujerShorts.html', {'prendas': prendas})
def catalogo_mujerfaldas(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Faldas',
       subcategoria__categoria__grupo__nombre='MujerInferior',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Inferior(Mujer)/MujerFaldas.html', {'prendas': prendas})
def catalogo_mujerjeans(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Jeans',
       subcategoria__categoria__grupo__nombre='MujerInferior',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Inferior(Mujer)/MujerJeans.html', {'prendas': prendas})
def catalogo_mujerpantalones(request):
   prendas = Prenda.objects.filter(
       subcategoria__nombre='Pantalones',
       subcategoria__categoria__grupo__nombre='MujerInferior',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Inferior(Mujer)/MujerPantalones.html', {'prendas': prendas})
def catalogo_mujervestidos(request):
   prendas = Prenda.objects.filter(
       subcateria__nombre='Vestidos',
       subcategoria__categoria__grupo__nombre='MujerRopa',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Ropa(Mujer)/MujerVestidos.html', {'prendas': prendas})
def catalogo_mujertops(request):
   prendas = Prenda.objects.filter(
       subcateria__nombre='Tops',
       subcategoria__categoria__grupo__nombre='MujerRopa',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Ropa(Mujer)/MujerTops.html', {'prendas': prendas})
def catalogo_mujerenterizos(request):
   prendas = Prenda.objects.filter(
       subcateria__nombre='Enterizos',
       subcategoria__categoria__grupo__nombre='MujerRopa',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Ropa(Mujer)/MujerEnterizos.html', {'prendas': prendas})
def catalogo_mujercamisetas(request):
   prendas = Prenda.objects.filter(
       subcateria__nombre='Camisetas',
       subcategoria__categoria__grupo__nombre='MujerRopa',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Ropa(Mujer)/MujerCamisetas.html', {'prendas': prendas})
def catalogo_mujercamisas(request):
   prendas = Prenda.objects.filter(
       subcateria__nombre='Camisas',
       subcategoria__categoria__grupo__nombre='MujerRopa',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Ropa(Mujer)/MujerCamisas.html', {'prendas': prendas})
def catalogo_mujerchaquetas(request):
   prendas = Prenda.objects.filter(
       subcateria__nombre='Chaquetas',
       subcategoria__categoria__grupo__nombre='MujerRopa',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Ropa(Mujer)/MujerChaquetas.html', {'prendas': prendas})
def catalogo_mujerblusas(request):
   prendas = Prenda.objects.filter(
       subcateria__nombre='Blusas',
       subcategoria__categoria__grupo__nombre='MujerRopa',
       disponible=True
   )
   return render(request, 'categorias/Mujer/Ropa(Mujer)/MujerBlusas.html', {'prendas': prendas})











