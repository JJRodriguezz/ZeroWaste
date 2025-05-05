from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('inventario/', views.lista_prendas, name='lista_prendas'), 
    path('contacto/', views.contacto, name='contacto'),
    path('catalogo/camisetas/', views.catalogo_camisetas, name='catalogo_camisetas'),
    path('catalogo/pantalones/', views.catalogo_pantalones, name='catalogo_pantalones'),
    path('catalogo/bolsosycarteras/', views.catalogo_bolsosycarteras, name='catalogo_bolsosycarteras'),
]