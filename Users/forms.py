# forms.py

from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import ModelForm, DateInput
from .models import Categoria, Usuarios
from Tienda.models import Libro

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['username', 'password', 'pnombre', 'snombre', 'papellido', 'sapellido', 'fecha_nacimiento', 'correo']
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nacimiento': DateInput(attrs={'type': 'date'}),
            'correo': forms.EmailInput(attrs={'type': 'email'})  # Especifica que el campo es de tipo email
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['autor', 'nombre_libro', 'fecha_publicacion', 'categoria', 'disponible_para_venta', 'precio', 'portada', 'resumen']

        widgets = {
            'fecha_publicacion': DateInput(attrs={'type': 'date'})
        }

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Seleccione una categoría")


class EditProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password1 = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Usuarios
        fields = ['username', 'correo', 'pnombre', 'snombre', 'papellido', 'sapellido', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if password or new_password1 or new_password2:
            if not self.instance.check_password(password):
                self.add_error('password', 'Contraseña actual incorrecta.')
            if new_password1 != new_password2:
                self.add_error('new_password2', 'Las nuevas contraseñas no coinciden.')

        return cleaned_data