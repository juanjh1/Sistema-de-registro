# Generated by Django 5.2.1 on 2025-05-17 10:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='perfil/')),
                ('numerotelefonico', models.CharField(max_length=50, null=True)),
                ('genero', models.CharField(max_length=10, null=True)),
                ('direccion', models.CharField(max_length=60, null=True)),
                ('fechanacimiento', models.DateField(null=True)),
                ('instagram', models.URLField(null=None)),
                ('facebook', models.URLField(null=None)),
                ('twiter', models.URLField(null=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
