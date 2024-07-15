from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views  # Asegúrate de tener esta línea
from django.conf.urls.static import static
from . import views
from Users import views as user_views
from Inicio import views as inicio_views

urlpatterns = [
    path('fantasia/', views.store_fantasia, name='store_fantasia'),
    path('ficcion/', views.store_ficcion, name='store_ficcion'),
    path('clasica/', views.store_clasica, name='store_clasica'),
    path('inicio/', inicio_views.helloworld, name='inicio'),
    path('checkout/', views.checkout, name= 'checkout'),
   
    path('finalizar_compra/', views.finalizar_compra, name= 'finalizar_compra'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('agregar/<int:libro_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:libro_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:libro_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
]

# Sirve los archivos estáticos en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)