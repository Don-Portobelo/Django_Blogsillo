# forms.py en la app 'publicar'
from django import forms
from .models import Publicacion
from Tienda.models import Libro

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['es_resumen', 'titulo', 'cuerpo', 'id_libro', 'portada']  # Incluir el campo 'portada'

        widgets = {
            'es_resumen': forms.RadioSelect(choices=[(True, 'Resumen'), (False, 'Crítica')]),
            'id_libro': forms.SelectMultiple(attrs={'size': 5}),  # Permitir selección múltiple
        }

    id_libro = forms.ModelMultipleChoiceField(queryset=Libro.objects.all(), label="Seleccionar Libros")