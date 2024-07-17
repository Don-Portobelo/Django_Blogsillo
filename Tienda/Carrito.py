# carrito.py
from .models import Libro, OrdenDeCompra
from Users.models import Usuarios

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, libro):
        id = str(libro.id_libro)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "libro_id": libro.id_libro,
                "nombre": libro.nombre_libro,
                "acumulado": libro.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += libro.precio
        self.guardar_carrito()
        

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, libro):
        id = str(libro.id_libro)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, libro):
        id = str(libro.id_libro)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= libro.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(libro)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    

    def calcular_total(self):
        total = sum(item['acumulado'] for item in self.carrito.values())
        return total

    def crear_orden(self, usuario):
        libros_carrito = []
        precio_total = 0
        nombre_items = ""

        for item_id, item_data in self.carrito.items():
            libro = Libro.objects.get(id_libro=item_data['libro_id'])
            cantidad = item_data['cantidad']
            subtotal = libro.precio * cantidad
            precio_total += subtotal
            nombre_items += f"{libro.nombre_libro} x {cantidad}, "

            libros_carrito.append({
                'libro': libro,
                'cantidad': cantidad,
                'subtotal': subtotal
            })

        return libros_carrito, precio_total

        


    def subir_orden(self, usuario):
        libros_carrito = []
        precio_total = 0
        nombre_items = ""

        for item_id, item_data in self.carrito.items():
            libro = Libro.objects.get(id_libro=item_data['libro_id'])
            cantidad = item_data['cantidad']
            subtotal = libro.precio * cantidad
            precio_total += subtotal
            nombre_items += f"{libro.nombre_libro} x {cantidad}, "

            libros_carrito.append({
                'libro': libro,
                'cantidad': cantidad,
                'subtotal': subtotal
            })

        # Crear la orden de compra
        orden_compra = OrdenDeCompra(
            nro_items=len(libros_carrito),
            nombre_items=nombre_items,
            precio_total=precio_total,
            usuarios_id_id=usuario,
            
        )
        orden_compra.save()

       

        return orden_compra
