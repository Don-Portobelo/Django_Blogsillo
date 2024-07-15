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


def detalle_publicacion(request, id_publicacion):
    publicacion = get_object_or_404(Publicacion, pk=id_publicacion)
    context = {
        'publicacion': publicacion
    }
    return render(request, 'detalle_publicacion.html', context)

def criticas_fantasia(request):
    # Filtrar las publicaciones que son críticas y pertenecen a libros de fantasía
    publicaciones = Publicacion.objects.filter(es_resumen=False, id_libro__categoria__nombre_categoria='Fantasia')

    context = {
        'publicaciones': publicaciones
    }
    return render(request, 'criticas_fantasia.html', context)

def criticas_chilenas(request):
    # Filtrar las publicaciones que son críticas y pertenecen a libros de fantasía
    publicaciones = Publicacion.objects.filter(es_resumen=False, id_libro__categoria__nombre_categoria='Literatura Chilena')

    context = {
        'publicaciones': publicaciones
    }
    return render(request, 'criticas_fantasia.html', context)