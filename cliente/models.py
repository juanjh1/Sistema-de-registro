from django.db import models
from uuid import uuid4

# Create your models here.

class InformacionUsuario (models.Model):
    numerotelefonico = models.CharField( max_length=50, null=False)
    genero = models.CharField(max_length=10, null=False)
    direccion = models.CharField(max_length=60, null=False)
    fechanacimiento = models.DateField(null=False)

    