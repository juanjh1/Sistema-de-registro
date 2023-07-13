from django.db import models
from empresa.models import Empresa
from persona.models import Persona
from  django.contrib.auth.models import User
from uuid import uuid4
import json

class Marca(models.Model):
    codigo =  models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=180)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Marcas'


class Modelo(models.Model):
    codigo =  models.IntegerField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=180)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Modelos'
    def __str__(self):
        return self.descripcion + str(self.codigo)
    
class Estado(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    descripcion = models.CharField(max_length=180)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


class Vehiculo(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    numero_placa = models.CharField(max_length=10, null=False, unique=True)
    numeracion = models.CharField(max_length=10, null=False, unique=True)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='vehiculo_propietario')
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    año = models.IntegerField()
    conductor = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='vehiculo_conducido')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    



def importar_datos_desde_json():
    # Leer el archivo JSON de marcas
    with open('C:/Users/acer/OneDrive/Escritorio/program/trabajo/marcas.json') as archivo_marcas:
        marcas = json.load(archivo_marcas)
        for marca in marcas:
            Marca.objects.create(
                codigo=marca['codigo'],
                descripcion=marca['descripcion']
            )
    
    # Leer el archivo JSON de modelos
    with open('C:/Users/acer/OneDrive/Escritorio/program/trabajo/modelos.json') as archivo_modelos:
        modelos = json.load(archivo_modelos)
        for modelo in modelos:
            Modelo.objects.create(
                codigo=modelo['codigo'],
                marca_id=modelo['marca'],
                descripcion=modelo['descripcion']
            )