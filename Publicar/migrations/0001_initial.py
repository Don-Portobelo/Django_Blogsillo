# Generated by Django 5.0.6 on 2024-07-03 22:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tienda', '0002_alter_libro_precio_alter_ordendecompra_precio_total'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id_publicaciones', models.AutoField(primary_key=True, serialize=False)),
                ('es_resumen', models.BooleanField()),
                ('titulo', models.CharField(max_length=255)),
                ('cuerpo', models.TextField()),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('numero_like', models.IntegerField(blank=True, null=True)),
                ('numero_dislikes', models.IntegerField(blank=True, null=True)),
                ('id_libro', models.ManyToManyField(to='Tienda.libro')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
