# models.py
from django.db import models
from Users.models import Categoria, Usuarios


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=255)
    nombre_libro = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)  # ForeignKey hacia Categoria
    resumen = models.TextField(default='No hay resumen disponible aún')
    disponible_para_venta = models.BooleanField()
    precio = models.IntegerField()
    portada = models.ImageField(upload_to='portadas/')

    class Meta:
        db_table = 'libros'  # Nombre exacto de la tabla en phpMyAdmin

    def __str__(self):
        return self.nombre_libro


class OrdenDeCompra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    nro_items = models.IntegerField()
    nombre_items = models.CharField(max_length=1000)
    precio_total = models.IntegerField()
    usuarios_id_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)  # Cambio aquí
    estado = models.CharField(max_length=255, default='pendiente')  # Nueva columna



    def __str__(self):
        return f"Orden de Compra #{self.id_compra} - Usuario: {self.usuarios_id.username}"
