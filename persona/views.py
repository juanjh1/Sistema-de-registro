from django.shortcuts import render, redirect
import uuid
from . import models
from empresa.models import Empresa
# Create your views here.


def view_registrar (request): 



    tipo_de_documento =[
        'DNI',
        'RUC',
        'Carnet de Extranjería'
    ]

    context={
        'tipo_documento':tipo_de_documento,
        'empresas' : Empresa.objects.filter().all()
    }
    
    
    return render(request, 'reg_persona.html', context)


def registar (request):
    nombre = request.POST.get('nombre_persona')
    tipo_documento =  request.POST.get('tipo_documento')
    abreviatura =  request.POST.get('abreviatura')
    descripcion =  request.POST.get('descripcion')
    empresa = request.POST.get('empresa')
   
    print(nombre,tipo_documento,abreviatura,descripcion,empresa,sep='\n')
    
    uuid_empresa = empresa[-36:]
    objeto_uuid = uuid.UUID(uuid_empresa)

    
    models.TipoDocumento.objects.create(
      tipo_documento=tipo_documento,
       abreviatura=abreviatura,
       descripcion=descripcion
    )
    
    empresa=Empresa.objects.filter(codigo=objeto_uuid).first()
    print(empresa)
    

    tipo_docu = models.TipoDocumento.objects.filter(tipo_documento=tipo_documento).first()
    models.Persona.objects.create(
        nombre=nombre,
        empresa=empresa,
        tipodocumento = tipo_docu)

    return redirect('/home/')


def view_pesonas(request):

    context = {
        'personas' :models.Persona.objects.filter().all()
    }
    
    return render(request, 'view_persona.html', context)


def delete_persona(request, code):
    persona =  models.Persona.objects.filter(codigo=code).first() 

    