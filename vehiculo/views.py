from django.shortcuts import render,redirect
from . import models
from empresa.models import Empresa

from persona.models import Persona
import uuid
# Create your views here.


def  viewcreate_vehiculo(request): 
  context = {
        'empresas':Empresa.objects.all(),
        'personas':Persona.objects.all(),
        'modelos':models.Modelo.objects.all(),
        'marcas': models.Marca.objects.all()}
  return render(request, 'reg_vehiculo.html', context)


def  view_vehiculo(request):
 
 context = {
  
   'vehiculos':models.Vehiculo.objects.filter().all()
  
 }
 return render(request, 'list_vehiculo.html', context)


def create_vehiculo(request):
    numeracion = request.POST.get('numeracion')
    n_placa = request.POST.get('n_placa')
    propietario = request.POST.get('propietario')
    modelo = request.POST.get('modelo')
    empresa = request.POST.get('empresa')
    ano_fabricacion = request.POST.get('ano_fabricacion')
    conductor = request.POST.get('conductor')

    ano_fabricacion =int(ano_fabricacion[0:3]) 

    uuid_empresa = empresa[-36:]
    empresa_uuid = uuid.UUID(uuid_empresa)

    uuid_propietario = propietario[-36:]
    propietario_uuid = uuid.UUID(uuid_propietario)

    uuid_conductor = conductor[-36:]
    conductor_uuid = uuid.UUID(uuid_conductor)

    uuid_modelo = modelo[-36:]
    modelo_uuid = uuid.UUID(uuid_modelo)

    empresa = Empresa.objects.filter(codigo=empresa_uuid).first()
    propietario = Persona.objects.filter(codigo=propietario_uuid).first()
    conductor = Persona.objects.filter(codigo=conductor_uuid).first()
    modelo = models.Modelo.objects.filter(codigo=modelo_uuid).first()

    models.Vehiculo.objects.create(
        empresa=empresa,
        numero_placa=n_placa,
        numeracion=numeracion,
        propietario=propietario,
        modelo=modelo,
        año=ano_fabricacion,
        conductor=conductor
    )
    return redirect('/home/')

def delete_vehiculo(request, code):

    vehiculo = models.Vehiculo.objects.filter(codigo=code).first()

    vehiculo.delete()
    return redirect('/home/')


def view_actualizar(request,code):
  context={
        'vehiculo': models.Vehiculo.objects.filter(codigo=code).first(),
        'empresas':Empresa.objects.all(),
        'personas':Persona.objects.all(),
        'modelos':models.Modelo.objects.all(),
        'marcas': models.Marca.objects.all()
    }
  
  return render(request, 'actualizar_vehiculo.html', context)
