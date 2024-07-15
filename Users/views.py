from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import UsuarioForm, CategoriaForm, LibroForm  # Importar múltiples formularios de forma más compacta
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required  # Importar el decorador
from django.http import JsonResponse

from Tienda.Carrito import Carrito
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import EditProfileForm
import logging
from Tienda.models import Libro, OrdenDeCompra
from .models import Usuarios, Reportes
from Tienda.forms import OrdenDeCompra

from django.conf import settings  # Asegurarse de importar la configuración de Django
import mercadopago

@login_required
def cuenta_usuario(request):
    return render(request, 'cuenta_usuario.html')


@staff_member_required
@login_required
def cuenta_admin(request):
    return render(request, 'cuenta_admin.html')


@login_required  # Asegura que el usuario esté autenticado para acceder a esta vista
def enviar_reporte(request):
    if request.method == 'POST':
        # Obtener el usuario actual que está enviando el reporte
        usuario = request.user  # Esto obtiene el objeto del usuario autenticado

        # Obtener los datos del formulario
        titulo = request.POST.get('titulo')
        motivo = request.POST.get('motivo')
        datos_motivo = request.POST.get('datos_motivo')
        cuerpo = request.POST.get('cuerpo')
        
        # Guardar los datos en la base de datos junto con el usuario
        reporte = Reportes.objects.create(
            titulo_reporte=titulo,
            motivo=motivo,
            datos_motivo=datos_motivo,
            cuerpo_reporte=cuerpo,
            usuario=usuario  # Asociar el usuario al reporte
        )
        
        # Redireccionar o mostrar un mensaje de éxito
        return redirect('cuenta_admin')  # Cambia 'inicio' por la URL a la que deseas redireccionar

    # Si el método no es POST, renderizar el formulario vacío
    return render(request, 'reportes.html')


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            new_password1 = form.cleaned_data.get('new_password1')
            if new_password1:
                user.set_password(new_password1)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('perfil')  # Redirige a una página de perfil después de la edición
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'editar_perfil.html', {'form': form})


def historial_reportes(request):
    return render(request, 'historial_reportes.html')

@login_required
def cargar_reportes(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        reportes = Reportes.objects.all().values('titulo_reporte', 'motivo', 'datos_motivo', 'cuerpo_reporte', 'usuario__username')
        return JsonResponse({'reportes': list(reportes)})
    return JsonResponse({'error': 'Bad request'}, status=400)



def obtener_detalles_carrito(carrito):
    detalles = []
    precio_total = 0  # Inicializar el precio total
    
    try:
        for item_id, item_data in carrito.items():
            libro = get_object_or_404(Libro, id_libro=item_data['libro_id'])
            cantidad = item_data.get('cantidad', 1)  # Puedes establecer una cantidad predeterminada si no está presente
            subtotal = libro.precio * cantidad
            precio_total += subtotal
            detalle_libro = f'"{libro.nombre_libro}" X {cantidad} = "{cantidad * libro.precio}"'
            detalles.append(detalle_libro)
    except Exception as e:
        print(f"Error al obtener detalles del carrito: {e}")
        precio_total = 0
    
    return ', '.join(detalles), precio_total

@login_required
def pagar(request):
    carrito_session = request.session.get('carrito', {})  # Obtener el carrito de la sesión
    carrito = Carrito(request)  # Instanciar el carrito usando la clase Carrito

    try:
        cadena_libros, total_compra = obtener_detalles_carrito(carrito_session)
    except Exception as e:
        print(f"Error al obtener detalles del carrito: {e}")
        cadena_libros = ""

    mp = mercadopago.MP(settings.MERCADOPAGO_ACCESS_TOKEN)

    preference = {
        "items": [
            {
                "id": "1",
                "title": cadena_libros,
                "description": "Libros de la compra",
                "quantity": 1,
                "currency_id": "CLP",
                "unit_price": total_compra,
            }
        ],
        "back_urls": {
            "success": "http://localhost:8000/tienda/store_fantasia/",
            "failure": "http://localhost:8000/tienda/store_fantasia/",
            "pending": "http://localhost:8000/tienda/store_fantasia/"
        },
        "auto_return": "approved"
    }

    try:
        preference_result = mp.create_preference(preference)
        return render(request, 'pagos.html', {'preference_id': preference_result['response']['id']})
    except Exception as e:
        print(f"Error al crear preferencia de pago: {e}")
        messages.error(request, "Hubo un error al procesar el pago. Por favor, inténtalo de nuevo más tarde.")
        return redirect('inicio')

def ingresar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save()  # Guarda el libro en la base de datos
            return redirect('cuenta_admin', id_libro=libro.id_libro)  # Redirige a la página de detalle del libro
    else:
        form = LibroForm()
    
    return render(request, 'ingresar_libro.html', {'form': form})




def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            try:
                usuario = form.save(commit=False)
                usuario.password = make_password(form.cleaned_data['password'])
                usuario.save()
                messages.success(request, 'Usuario registrado exitosamente')
                return redirect('login')  # Cambia 'login' a la URL correspondiente después del registro
            except Exception as e:
                messages.error(request, f'Error al guardar el usuario: {e}')
        else:
            messages.error(request, f'Formulario inválido: {form.errors}')
    else:
        form = UsuarioForm()
    
    return render(request, 'Registro_Usuario.html', {'form': form})


# Agrega la vista de perfil
def profile(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('cuenta_admin')
        else:
            return redirect('cuenta_usuario')
    else:
        return redirect('login')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return HttpResponse('Usuario o contraseña incorrectos')
    return render(request, 'login.html')



def index(request):
    return render(request, 'index.php')

def ingresar_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        print("Datos del formulario:", request.POST)  # Imprimir los datos del formulario
        if form.is_valid():
            print("Formulario válido, guardando...")  # Confirmar que el formulario es válido
            form.save()
            print("Guardado exitoso")  # Confirmar que el guardado fue exitoso
            return redirect('ingresa_categoria')
        else:
            print("Formulario inválido:", form.errors)  # Imprimir los errores del formulario
    else:
        form = CategoriaForm()
    
    return render(request, 'Ingresar_Categoria.html', {'form': form})
