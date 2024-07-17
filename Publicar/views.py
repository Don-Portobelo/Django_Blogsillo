from django.shortcuts import render, redirect
from .forms import PublicacionForm
from Users.models import Categoria
from Tienda.models import Libro
from .models import Publicacion
# Create your views here.


# views.py en la app 'publicar'
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PublicacionForm

@login_required
def publicar(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.id_usuario = request.user
            publicacion.save()
            form.save_m2m()  # Guardar relaciones ManyToMany
            return redirect('inicio')  # Reemplazar con la vista a la que deseas redirigir después de guardar
    else:
        form = PublicacionForm()
    return render(request, 'publicar.html', {'form': form})

def c_criticas(request):
    
    return render(request, 'c_criticas.html')


def c_resumenes(request):
    
    return render(request, 'c_resumenes.html')

def detalle_publicacion(request, id_publicacion):
    publicacion = get_object_or_404(Publicacion, pk=id_publicacion)
    context = {
        'publicacion': publicacion
    }
    return render(request, 'detalle_publicacion.html', context)

from django.http import JsonResponse

def criticas_fantasia(request):
    publicaciones = Publicacion.objects.filter(es_resumen=False, id_libro__categoria__nombre_categoria='Fantasia')
    print("Criticas Fantasia:", publicaciones)  # Registro de depuración
    context = {
        'publicaciones': publicaciones,
        'titulo': 'Críticas de Fantasía'
    }
    return render(request, 'criticas_fantasia.html', context)

def criticas_chilenas(request):
    publicaciones = Publicacion.objects.filter(es_resumen=False, id_libro__categoria__nombre_categoria='Literatura Chilena')
    print("Criticas Chilenas:", publicaciones)  # Registro de depuración
    context = {
        'publicaciones': publicaciones,
        'titulo': 'Críticas de Literatura Chilena'
    }
    return render(request, 'criticas_fantasia.html', context)

def criticas_ciencia(request):
    publicaciones = Publicacion.objects.filter(es_resumen=False, id_libro__categoria__nombre_categoria='Ciencia Ficcion')
    print("Criticas Ciencia Ficcion:", publicaciones)  # Registro de depuración
    context = {
        'publicaciones': publicaciones,
        'titulo': 'Críticas de Ciencia Ficción'
    }
    return render(request, 'criticas_fantasia.html', context)

def resumenes_fantasia(request):
    publicaciones = Publicacion.objects.filter(es_resumen=True, id_libro__categoria__nombre_categoria='Fantasia')
    print("Resumenes Fantasia:", publicaciones)  # Registro de depuración
    context = {
        'publicaciones': publicaciones,
        'titulo': 'Resúmenes de Fantasía'
    }
    return render(request, 'criticas_fantasia.html', context)

def resumenes_chilenas(request):
    publicaciones = Publicacion.objects.filter(es_resumen=True, id_libro__categoria__nombre_categoria='Literatura Chilena')
    print("Resumenes Chilenas:", publicaciones)  # Registro de depuración
    context = {
        'publicaciones': publicaciones,
        'titulo': 'Resúmenes de Literatura Chilena'
    }
    return render(request, 'criticas_fantasia.html', context)

def resumenes_ciencia(request):
    publicaciones = Publicacion.objects.filter(es_resumen=True, id_libro__categoria__nombre_categoria='Ciencia Ficcion')
    print("Resumenes Ciencia Ficcion:", publicaciones)  # Registro de depuración
    context = {
        'publicaciones': publicaciones,
        'titulo': 'Resúmenes de Ciencia Ficción'
    }
    return render(request, 'criticas_fantasia.html', context)