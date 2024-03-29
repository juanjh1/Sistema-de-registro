from django.db import models
from uuid import uuid4
from  django.contrib.auth.models import User
# Create your models here.

class Empresa(models.Model):
    codigo =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField( max_length=50)
    direccion = models.CharField(null=False, max_length=70)
    flota = models.CharField( max_length=50, null=False)
    correo_electronico = models.EmailField( max_length=254, null=False)
    numero_resolucion = models.CharField(null=False, max_length=100)
    fecha_resolucion = models.DateField(null=False)
    fecha_creacion = models.DateTimeField( auto_now=True)
    fecha_actualizacion = models.DateTimeField( auto_now=True)
    federacion = models.CharField( max_length=50, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
       return self.nombre + str(self.codigo)

    class Meta:
        verbose_name_plural = "Empresas"

class Federacion (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField( max_length=50)
    fecha_creacion = models.DateTimeField( auto_now=True)
    fecha_actualizacion = models.DateTimeField( auto_now=True)
    
    def __str__(self) -> str:
       return self.nombre + str(self.id)

    class Meta:
        verbose_name_plural = "Federaciones"

def file_upload_path(instance, filename):
    # Define la ruta donde se almacenarán los archivos
    return f'media/pdfs/{uuid4()}/{filename}'

class Licencia(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    numero_resolucion = models.CharField(null=False, max_length=100)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    Recibo_caja = models.CharField(max_length=180)
    pdf = models.FileField(upload_to=file_upload_path, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.empresa) + str(self.codigo)

    class Meta:
        verbose_name_plural = "Licencias"


class Paradero(models.Model):
    codigo =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre =  models.CharField( max_length=50)
    numero_resolucion = models.CharField(null=False, max_length=100)
    fecha_resolcuion = models.DateField()
    fecha_creacion = models.DateTimeField( auto_now=True)
    fecha_actualizacion = models.DateTimeField( auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Empresa_paradero(models.Model):
    empresa = models.ForeignKey(Empresa ,on_delete=models.CASCADE)
    paradero= models.ForeignKey(Paradero ,on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField( auto_now=True)
    fecha_actualizacion = models.DateTimeField( auto_now=True)
     
    
