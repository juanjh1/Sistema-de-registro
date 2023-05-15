from django.shortcuts import render,redirect
from . import models
from empresa.models import Empresa
from  django.contrib.auth.models import User
from persona.models import Persona
import uuid
from django.shortcuts import render, get_object_or_404
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
    estado = request.POST.get('estado')

    ano_fabricacion =int(ano_fabricacion[0:3]) 

    empresa_uuid = uuid.UUID(empresa)

    
    propietario_uuid = uuid.UUID(propietario)

    
    conductor_uuid = uuid.UUID(conductor)

    estado_uuid = uuid.UUID(estado)
    
    estado=  models.Estado.objects.filter(codigo=estado_uuid).first()
    empresa = Empresa.objects.filter(codigo=empresa_uuid).first()
    propietario = Persona.objects.filter(codigo=propietario_uuid).first()
    conductor = Persona.objects.filter(codigo=conductor_uuid).first()
    modelo = models.Modelo.objects.filter(codigo=modelo).first()

    usuario = User.objects.filter(id=request.user.id).first()

    models.Vehiculo.objects.create(
        empresa=empresa,
        numero_placa=n_placa,
        numeracion=numeracion,
        propietario=propietario,
        modelo=modelo,
        año=ano_fabricacion,
        conductor=conductor,
        usuario= usuario,
        estado= estado
    )
    return redirect('/home/')
  
  context = {
        'empresas':Empresa.objects.all(),
        'personas':Persona.objects.all(),
        'modelos':models.Modelo.objects.all(),
        'marcas': models.Marca.objects.all(),
        'estados': models.Estado.objects.all()}
  
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
        'marcas': models.Marca.objects.all(),
        'estados': models.Estado.objects.all()
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

    


    empresa = Empresa.objects.filter(codigo=empresa_uuid).first()
    propietario = Persona.objects.filter(codigo=propietario_uuid).first()
    conductor = Persona.objects.filter(codigo=conductor_uuid).first()
    modelo = models.Modelo.objects.filter(codigo=modelo).first()

    estado = models.Estado.objects.filter(codigo=modelo).first()

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

def vehiculo_detail(request, code):
    vehiculo = get_object_or_404(models.Vehiculo, pk=code)
    return render(request, 'vehiculo_detail.html', {'vehiculo': vehiculo})