from django.shortcuts import render,redirect
from . import models
from empresa.models import Empresa

from persona.models import Persona
import uuid
# Create your views here.


def  create_vehiculo(request): 

  if request.method == 'POST':
    numeracion = request.POST.get('numeracion')
    n_placa = request.POST.get('n_placa')
    propietario = request.POST.get('propietario')
    modelo = request.POST.get('modelo')
    empresa = request.POST.get('empresa')
    ano_fabricacion = request.POST.get('ano_fabricacion')
    conductor = request.POST.get('conductor')

    ano_fabricacion =int(ano_fabricacion[0:3]) 

    empresa_uuid = uuid.UUID(empresa)

    
    propietario_uuid = uuid.UUID(propietario)

    
    conductor_uuid = uuid.UUID(conductor)

   
    modelo_uuid = uuid.UUID(modelo)

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

def actualizar(request, code):
   
    numeracion = request.POST.get('numeracion')
    n_placa = request.POST.get('n_placa')
    propietario = request.POST.get('propietario')
    modelo = request.POST.get('modelo')
    empresa = request.POST.get('empresa')
    ano_fabricacion = request.POST.get('ano_fabricacion')
    conductor = request.POST.get('conductor')


    ano_fabricacion =int(ano_fabricacion[0:4]) 
    

    empresa_uuid = uuid.UUID(empresa)

  
    propietario_uuid = uuid.UUID(propietario)

    
    conductor_uuid = uuid.UUID(conductor)

    
    modelo_uuid = uuid.UUID(modelo)

    empresa = Empresa.objects.filter(codigo=empresa_uuid).first()
    propietario = Persona.objects.filter(codigo=propietario_uuid).first()
    conductor = Persona.objects.filter(codigo=conductor_uuid).first()
    modelo = models.Modelo.objects.filter(codigo=modelo_uuid).first()

    vehiculo = models.Vehiculo.objects.filter(codigo = code).first()


    vehiculo.numeracion = numeracion
    vehiculo.numero_placa = n_placa
    vehiculo.empresa = empresa
    vehiculo.año = ano_fabricacion
    vehiculo.modelo = modelo
    vehiculo.propietario = propietario
    vehiculo.conductor = conductor

    vehiculo.save()

    return redirect('/home/')