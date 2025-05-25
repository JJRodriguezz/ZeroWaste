from .models import Prenda

def prendas_recomendadas(request):
    """Añade las prendas recomendadas al contexto de todas las templates."""
    prendas = Prenda.objects.filter(disponible=True).order_by('?')[:5]
    return {'prendas_recomendadas': prendas} 