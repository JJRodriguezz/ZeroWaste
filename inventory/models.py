from django.db import models

# Create your models here.

class Prenda(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=50) #Ej: "nueva", "En buen estado", etc...
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='prendas/')
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
