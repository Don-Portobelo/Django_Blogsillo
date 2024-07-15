from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Libro, Categoria
from .forms import OrdenDeCompraForm
from .Carrito import Carrito
from Users.views import pagar
from Users.models import Usuarios
import json
import logging

logger = logging.getLogger(__name__)

@login_required
def store_fantasia(request):
    try:
        categoria_fantasia = Categoria.objects.get(id_categoria=1)
        libros = Libro.objects.filter(categoria=categoria_fantasia, disponible_para_venta=True)
        carrito = request.session.get('carrito', [])
        return render(request, 'store_fantasia.html', {'libros': libros, 'carrito': carrito})
    except Categoria.DoesNotExist:
        mensaje_error = "No se ha agregado ningun libro del genero fantasia para la venta"
        return render(request, 'error.html', {'mensaje_error': mensaje_error})

@login_required
def store_ficcion(request):
    try:
        categoria_ficcion = Categoria.objects.get(id_categoria=5)
        libros = Libro.objects.filter(categoria=categoria_ficcion, disponible_para_venta=True)
        carrito = request.session.get('carrito', [])
        return render(request, 'store_ficcion.html', {'libros': libros, 'carrito': carrito})
    except Categoria.DoesNotExist:
        mensaje_error = "No se ha agregado ningun libro del genero ficcion para la venta"
        return render(request, 'error.html', {'mensaje_error': mensaje_error})


@login_required
def store_clasica(request):
    try:
        categoria_clasica = Categoria.objects.get(id_categoria=6)
        libros = Libro.objects.filter(categoria=categoria_clasica, disponible_para_venta=True)
        carrito = request.session.get('carrito', [])
        return render(request, 'store_clasica.html', {'libros': libros, 'carrito': carrito})
    except Categoria.DoesNotExist:
        mensaje_error = "No se ha agregado ningun libro del genero ficcion para la venta"
        return render(request, 'error.html', {'mensaje_error': mensaje_error})



@login_required  # Asegúrate de que el usuario esté autenticado
def finalizar_compra(request):
    carrito = Carrito(request)
    usuario = request.user  # Asegúrate de que el usuario esté autenticado

    try:
        usuario = Usuarios.objects.get(id_usuario=request.user.id_usuario)  # Ajuste aquí
        orden_compra = carrito.crear_orden(usuario)
        # Aquí puedes agregar cualquier lógica adicional, como redirigir a una página de confirmación
        return redirect('pagar')  # Redirigir a una página de confirmación o similar
    except Usuarios.DoesNotExist:
        # Manejar el caso en que el usuario no exista en la tabla Usuarios
        return redirect('pagar')




def agregar_producto(request, libro_id):
    carrito = Carrito(request)
    libro = get_object_or_404(Libro, id_libro=libro_id)
    carrito.agregar(libro)
    return redirect('store_fantasia')  # Redirige a la página de tu tienda o la página que prefieras

def eliminar_producto(request, libro_id):
    carrito = Carrito(request)
    libro = get_object_or_404(Libro, id_libro=libro_id)
    carrito.eliminar(libro)
    return redirect('store_fantasia')  # Redirige a la página de tu tienda o la página que prefieras

def restar_producto(request, libro_id):
    carrito = Carrito(request)
    libro = get_object_or_404(Libro, id_libro=libro_id)
    carrito.restar(libro)
    return redirect('store_fantasia')  # Redirige a la página de tu tienda o la página que prefieras

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('store_fantasia')  # Redirige a la página de tu tienda o la página que prefieras


@login_required
def checkout(request):
    try:
        carrito = request.session.get('carrito', {})
        libros_carrito = []
        total_carrito = 0

        for item_id, item_data in carrito.items():
            libro = get_object_or_404(Libro, id_libro=item_data['libro_id'])
            cantidad = item_data.get('cantidad', 1)
            subtotal = libro.precio * cantidad
            total_carrito += subtotal
            libros_carrito.append({
                'libro': libro,
                'cantidad': cantidad,
                'subtotal': subtotal
            })

        if request.method == 'POST':
            form = OrdenDeCompraForm(request.POST)

            if form.is_valid():
                correo_usuario = form.cleaned_data['correo_usuario']
                usuario = get_object_or_404(Usuarios, correo=correo_usuario)
                nombre_items = ', '.join([f"{item['cantidad']} x {item['libro'].nombre_libro}" for item in libros_carrito])

                orden_compra = form.save(commit=False)
                orden_compra.nro_items = sum([item['cantidad'] for item in carrito.values()])
                orden_compra.nombre_items = nombre_items
                orden_compra.precio_total = total_carrito
                orden_compra.usuarios_id = usuario

                orden_compra.save()
                del request.session['carrito']
                return redirect('pagar')

        else:
            form = OrdenDeCompraForm()

        return render(request, 'checkout.html', {'libros_carrito': libros_carrito, 'total_carrito': total_carrito, 'form': form})

    except Exception as e:
        logger.error(f"Error en checkout: {e}")
        return render(request, 'error.html', {'mensaje_error': 'Hubo un error al procesar el checkout. Por favor, intenta de nuevo.'})