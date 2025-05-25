from django.urls import path
from .views import login_view, logout_view
from . import views
from django.contrib.auth import views as auth_views
from .views import perfil_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil_view, name='perfil'),
    path('cambiar-contrasena/', auth_views.PasswordChangeView.as_view(
        template_name='users/cambiar_contrasena.html',
        success_url='/users/cambio-exitoso/'
    ), name='cambiar_contrasena'),
    path('cambio-exitoso/', auth_views.PasswordChangeDoneView.as_view(
        template_name='users/cambio_exitoso.html'
    ), name='cambio_exitoso'),
]
