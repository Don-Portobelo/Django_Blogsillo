# Generated by Django 5.0.6 on 2024-06-25 06:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]