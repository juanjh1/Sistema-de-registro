from django.db import models
from uuid import uuid4
from  django.contrib.auth.models import User
# Create your models here.

class Empresa(models.Model):
    codigo =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField( max_length=50)
    direccion = models.CharField(null=False, max_length=70)
    flota = models.IntegerField(null=False)
    correo_electronico = models.EmailField( max_length=254, null=False)
    numero_resolucion = models.CharField(null=False, max_length=100)
    fecha_resolucion = models.DateField(null=False)
    fecha_creacion = models.DateTimeField( auto_now=True)
    fecha_actualizacion = models.DateTimeField( auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
       return self.nombre + str(self.codigo)

    class Meta:
        verbose_name_plural = "Empresas"

class Federacion (models.Model):
    codigo =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField( max_length=50)
    fecha_creacion = models.DateTimeField( auto_now=True)
    fecha_actualizacion = models.DateTimeField( auto_now=True)
    
    def __str__(self) -> str:
       return self.nombre + str(self.codigo)

    class Meta:
        verbose_name_plural = "Federaciones"

class Licencia(models.Model):
    codigo =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
    numero_resolucion = models.CharField(null=False, max_length=100)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    Recibo_caja = models.CharField(max_length=180)
    empresa = models.ForeignKey( Empresa , on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField( auto_now=True)
    fecha_actualizacion = models.DateTimeField( auto_now=True)
    def __str__(self) -> str:
       return self.nombre + str(self.codigo)

    class Meta:
        verbose_name_plural = "Licencias"


class Paradero(models.Model):
    codigo =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre =  models.CharField( max_length=50)
    numero_resolucion = models.CharField(null=False, max_length=100)
    fecha_resolcuion = models.DateField()
    fecha_creacion = models.DateTimeField( auto_now=True)
    fecha_actualizacion = models.DateTimeField( auto_now=True)

class Empresa_paradero(models.Model):
    empresa = models.ForeignKey(Empresa ,on_delete=models.CASCADE)
    paradero= models.ForeignKey(Paradero ,on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField( auto_now=True)
    fecha_actualizacion = models.DateTimeField( auto_now=True)
     
    
