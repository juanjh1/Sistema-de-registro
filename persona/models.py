from django.db import models
from uuid import uuid4
from empresa.models import Empresa
from  django.contrib.auth.models import User


class TipoDocumento(models.Model):
    DOCUMENTO_CHOICES = [
        ('DNI', 'DNI'),
        ('RUC', 'RUC'),
        ('CARNET', 'Carnet de Extranjería'),
    ]
    tipo_documento = models.CharField(max_length=10, choices=DOCUMENTO_CHOICES)
    descripcion = models.CharField(max_length=90)


    def __str__(self):
        return self.tipo_documento

class Persona(models.Model):
    usuario = models.ForeignKey(User,  on_delete=models.CASCADE)
    codigo =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=10, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre + str(self.codigo)