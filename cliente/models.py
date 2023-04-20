from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class InformacionUsuario (models.Model):
    foto = models.ImageField( upload_to="perfil/", height_field=None, width_field=None, max_length=None, null=True,default="default_profile.png", blank=True)
    numerotelefonico = models.CharField( max_length=50, null=True)
    genero = models.CharField(max_length=10, null=True)
    direccion = models.CharField(max_length=60, null=True)
    fechanacimiento = models.DateField(null=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    