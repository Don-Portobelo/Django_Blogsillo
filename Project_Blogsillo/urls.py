"""
URL configuration for Project_Blogsillo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from Inicio import views as inicio_views
from Users import views as users_views
from Publicar import views as publicar_views
urlpatterns = [
   
    path('', inicio_views.helloworld, name='inicio'),
    path('registro/', users_views.registro_usuario, name= 'registro'),
     path('login/', auth_views.LoginView.as_view(template_name='Login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ingresar_categoria/', users_views.ingresar_categorias, name='ingresa_categoria'),
    path('usuario/', users_views.cuenta_usuario, name='cuenta_usuario'),
    path('enviar_reporte/', users_views.enviar_reporte, name='enviar_reporte'),
    path('admin/', users_views.cuenta_admin, name='cuenta_admin'),
    path('index/', users_views.index, name='index'),
    path('pagar/', users_views.pagar, name='pagar'),
    path('tienda/', include('Tienda.urls')),
    path('ingresar_libro/', users_views.ingresar_libro, name='ingresar_libro'),
    path('accounts/profile/', users_views.profile, name='profile'),
    path('cargar_reportes/', users_views.cargar_reportes, name='cargar_reportes'),
    path('historial_reportes/', users_views.historial_reportes, name='historial_reportes'),
    path('publicar/', publicar_views.publicar, name='publicar'),
    path('editar_perfil/', users_views.editar_perfil, name='editar_perfil'),
    path('c_criticas/', publicar_views.c_criticas, name='c_criticas'),
    path('criticas_fantasia/', publicar_views.criticas_fantasia, name='criticas_fantasia'),
     path('criticas_chilenas/', publicar_views.criticas_chilenas, name='criticas_chilenas'),
    path('publicacion/<int:id_publicacion>/', publicar_views.detalle_publicacion, name='detalle_publicacion'),
]


# Configurar la redirección después de iniciar sesión para administradores
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Configurar la redirección después de iniciar sesión para administradores
# Usando la configuración LOGIN_REDIRECT_URL
from django.urls import reverse_lazy

# Configurar la redirección después de iniciar sesión para administradores
# Usando la configuración LOGIN_REDIRECT_URL
from django.urls import reverse_lazy

# Redirigir al administrador después de iniciar sesión
LOGIN_REDIRECT_URL = 'cuenta_admin'