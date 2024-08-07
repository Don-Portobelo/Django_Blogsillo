# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'categoria'


class CategoriaLibro(models.Model):
    categoria = models.OneToOneField(Categoria, models.DO_NOTHING, primary_key=True)  # The composite primary key (categoria_id, libro_id) found, that is not supported. The first column is selected.
    libro = models.ForeignKey('Libros', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'categoria_libro'
        unique_together = (('categoria', 'libro'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Escritos(models.Model):
    id_escrito = models.AutoField(primary_key=True)
    es_resumen = models.CharField(max_length=1)
    titulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateField()
    numero_like = models.IntegerField(blank=True, null=True)
    numero_dislikes = models.IntegerField(blank=True, null=True)
    libros_id_libro = models.ForeignKey('Libros', models.DO_NOTHING, db_column='libros_id_libro')
    usuarios_id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuarios_id_usuario')

    class Meta:
        managed = False
        db_table = 'escritos'


class Libros(models.Model):
    id_libro = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=255)
    nombre_libro = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    disponible_para_venta = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    portada = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    resumen = models.TextField()

    class Meta:
        managed = False
        db_table = 'libros'


class LibrosCompra(models.Model):
    libro = models.OneToOneField(Libros, models.DO_NOTHING, primary_key=True)  # The composite primary key (libro_id, compra_id) found, that is not supported. The first column is selected.
    compra = models.ForeignKey('OrdeDeCompra', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'libros_compra'
        unique_together = (('libro', 'compra'),)


class LibrosReportes(models.Model):
    libro = models.OneToOneField(Libros, models.DO_NOTHING, primary_key=True)  # The composite primary key (libro_id, reporte_id) found, that is not supported. The first column is selected.
    reporte = models.ForeignKey('Reportes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'libros_reportes'
        unique_together = (('libro', 'reporte'),)


class OrdeDeCompra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    nro_items = models.IntegerField()
    nombre_items = models.CharField(max_length=1000)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orde_de_compra'


class Reportes(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    titulo_reporte = models.CharField(max_length=255)
    motivo = models.CharField(max_length=255)
    datos_motivo = models.CharField(max_length=255)
    cuerpo_reporte = models.TextField()
    escritos_id_escrito = models.ForeignKey(Escritos, models.DO_NOTHING, db_column='escritos_id_escrito')
    orde_de_compra_id_compra = models.ForeignKey(OrdeDeCompra, models.DO_NOTHING, db_column='orde_de_compra_id_compra')
    usuarios_id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuarios_id_usuario')

    class Meta:
        managed = False
        db_table = 'reportes'


class TiendaCategoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tienda_categoria'


class TiendaLibro(models.Model):
    id = models.BigAutoField(primary_key=True)
    autor = models.CharField(max_length=255)
    nombre_libro = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    disponible_para_venta = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    portada = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tienda_libro'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    es_admin = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=255)
    snombre = models.CharField(max_length=255, blank=True, null=True)
    papellido = models.CharField(max_length=255)
    sapellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    correo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'usuarios'
