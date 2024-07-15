from django.db import models
from django.conf import settings
from Tienda.models import Libro
# Create your models here.


class Publicacion(models.Model):
    id_publicaciones = models.AutoField(primary_key=True)
    es_resumen = models.BooleanField()
    titulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    numero_like = models.IntegerField(null=True, blank=True)
    numero_dislikes = models.IntegerField(null=True, blank=True)
    id_libro = models.ManyToManyField('Tienda.Libro')  # Referencia correcta al modelo Libro en la app Tienda
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Referencia correcta al modelo de usuario
    portada = models.ImageField(upload_to='portadas_publicaciones/', null=True, blank=True)  # Nuevo campo para la imagen, ahora opcional
    def __str__(self):
        return self.titulo
