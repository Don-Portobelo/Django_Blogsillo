from django.db import migrations,models
from django.utils import timezone
from django.conf import settings  # Importa settings para acceder a AUTH_USER_MODEL 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'categoria'  # Especifica el nombre de la tabla

    def __str__(self):
        return self.nombre_categoria

def add_default_last_login(apps, schema_editor):
    Usuarios = apps.get_model('Users', 'Usuarios')
    Usuarios.objects.filter(last_login__isnull=True).update(last_login=timezone.now())

class Migration(migrations.Migration):
    dependencies = [
        ('Users', '0001_initial.py'),  # Asegúrate de poner el nombre correcto de la última migración
    ]

    operations = [
        migrations.RunPython(add_default_last_login),
    ]

from django.contrib.auth.models import BaseUserManager

class UsuariosManager(BaseUserManager):
    def create_user(self, username, email, pnombre, papellido, fecha_nacimiento, password=None):
        if not email:
            raise ValueError('Los usuarios deben tener un correo electrónico')
        if not username:
            raise ValueError('Los usuarios deben tener un nombre de usuario')

        user = self.model(
            username=username,
            correo=self.normalize_email(email),
            pnombre=pnombre,
            papellido=papellido,
            fecha_nacimiento=fecha_nacimiento,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, pnombre, papellido, fecha_nacimiento, password=None):
        user = self.create_user(
            username=username,
            email=email,
            pnombre=pnombre,
            papellido=papellido,
            fecha_nacimiento=fecha_nacimiento,
            password=password,
        )
        user.es_admin = True  # Ensure es_admin is True for superusers
        user.save(using=self._db)
        return user

class Usuarios(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    es_admin = models.BooleanField(default=False)
    pnombre = models.CharField(max_length=255)
    snombre = models.CharField(max_length=255, null=True, blank=True)
    papellido = models.CharField(max_length=255)
    sapellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    last_login = models.DateTimeField(default=timezone.now)

    objects = UsuariosManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['correo', 'pnombre', 'papellido', 'fecha_nacimiento']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.es_admin

    @property
    def is_superuser(self):
        return self.es_admin  # Assuming superuser is determined by `es_admin`

    class Meta:
        db_table = 'usuarios'



class Reportes(models.Model):
    titulo_reporte = models.CharField(max_length=255)
    motivo = models.CharField(max_length=255)
    datos_motivo = models.CharField(max_length=255)
    cuerpo_reporte = models.TextField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Utiliza AUTH_USER_MODEL

    def __str__(self):
        return f'Reporte: {self.titulo_reporte} - Usuario: {self.usuario.username}'
