from django import forms
from Users.models import Usuarios
from .models import OrdenDeCompra

class OrdenDeCompraForm(forms.ModelForm):
    correo_usuario = forms.EmailField(label='Correo Electrónico', required=True)

    class Meta:
        model = OrdenDeCompra
        fields = []  # No incluir campos directamente en el formulario, los manejaremos manualmente

    def clean_correo_usuario(self):
        correo = self.cleaned_data.get('correo_usuario')
        try:
            usuario = Usuarios.objects.get(correo=correo)
            self.cleaned_data['usuario'] = usuario  # Guardamos el objeto completo del usuario
        except Usuarios.DoesNotExist:
            raise forms.ValidationError('No se encontró ningún usuario con este correo electrónico.')
        return correo

    def save(self, commit=True):
        orden = super().save(commit=False)
        orden.usuario_id = self.cleaned_data['usuario']  # Asignamos la instancia completa del usuario
        if commit:
            orden.save()
        return orden