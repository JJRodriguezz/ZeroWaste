from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('inventario/', views.lista_prendas, name='lista_prendas'), 
    path('contacto/', views.contacto, name='contacto')
]