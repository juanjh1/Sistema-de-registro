from django.db import models
from uuid import uuid4
from empresa.models import Empresa

class TipoDocumento(models.Model):
    DOCUMENTO_CHOICES = [
        ('DNI', 'DNI'),
        ('RUC', 'RUC'),
        ('CARNET', 'Carnet de Extranjería'),
    ]
    tipo_documento = models.CharField(max_length=10, choices=DOCUMENTO_CHOICES)
    abreviatura = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=90)

class Persona(models.Model):
    codigo =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=10, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)