from django.db import models
from django.utils import timezone

# Create your models here.

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.grupo})"
    
class Subcategoria(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        if self.nombre.lower() == self.categoria.nombre.lower():
            return self.nombre  # Evita redundancia
        return f"{self.nombre} ({self.categoria.nombre} - {self.categoria.grupo.nombre})"

class Prenda(models.Model):
    codigo = models.CharField(max_length=20, unique=True)  # nuevo campo para ID personalizada
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='prendas/')
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    fecha_venta = models.DateTimeField(null=True, blank=True)
    # NUEVA RELACIÓN
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.codigo