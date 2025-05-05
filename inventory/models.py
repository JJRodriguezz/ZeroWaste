from django.db import models

# Opciones de categorías tomadas del navbar (mujer, hombre, niño, bebé)
CATEGORIAS = [
    # Mujer - Ropa
    ('Blusas', 'Blusas'),
    ('Chaquetas', 'Chaquetas'),
    ('Camisas', 'Camisas'),
    ('Camisetas', 'Camisetas'),
    ('Enterizos', 'Enterizos'),
    ('Tops', 'Tops'),
    ('Vestidos', 'Vestidos'),

    # Mujer - Inferior
    ('Pantalones', 'Pantalones'),
    ('Jeans', 'Jeans'),
    ('Faldas', 'Faldas'),
    ('Shorts', 'Shorts'),
    ('Bodies', 'Bodies'),

    # Mujer - Especiales
    ('Trajes de baño', 'Trajes de baño'),
    ('Conjuntos', 'Conjuntos'),
    ('Deportivos', 'Deportivos'),
    ('Pijamas', 'Pijamas'),
    ('Ropa interior', 'Ropa interior'),

    # Mujer - Accesorios
    ('Bolsos y carteras', 'Bolsos y carteras'),
    ('Zapatos', 'Zapatos'),
    ('Sandalias', 'Sandalias'),
    ('Accesorios', 'Accesorios'),

    # Hombre - Ropa
    ('Camisas hombre', 'Camisas hombre'),
    ('Chaquetas hombre', 'Chaquetas hombre'),
    ('Pantalones hombre', 'Pantalones hombre'),
    ('Zapatos hombre', 'Zapatos hombre'),
    ('Deportivos hombre', 'Deportivos hombre'),
    ('Blazers', 'Blazers'),

    # Hombre - Extras
    ('Sandalias hombre', 'Sandalias hombre'),
    ('Accesorios hombre', 'Accesorios hombre'),
    ('Artículos hogar', 'Artículos hogar'),

    # Niño
    ('Camisas niño', 'Camisas niño'),
    ('Pantalones niño', 'Pantalones niño'),
    ('Chaquetas niño', 'Chaquetas niño'),
    ('Zapatos niño', 'Zapatos niño'),

    # Bebé
    ('Bodies bebé', 'Bodies bebé'),
    ('Conjuntos bebé', 'Conjuntos bebé'),
    ('Pijamas bebé', 'Pijamas bebé'),
]

class Prenda(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=50)  # Ej: "Como nueva"
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='prendas/')
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS,
        default='Camisetas'
    )

    def __str__(self):
        return self.nombre
