from django.shortcuts import render, redirect
import uuid
from . import models
from empresa.models import Empresa
from  django.contrib.auth.models import User
# Create your views here.


def view_registrar (request): 



    tipo_de_documento = models.TipoDocumento.objects.filter()

    context={
        'tipo_documento':tipo_de_documento,
        'empresas' : Empresa.objects.filter().all()
    }
    
    
    return render(request, 'reg_persona.html', context)


def registar (request):
    nombre = request.POST.get('nombre_persona')
    tipo_documento =  request.POST.get('tipo_documento')
    numero =  request.POST.get('numero_documento')
    descripcion =  request.POST.get('descripcion')
    empresa = request.POST.get('empresa')
   
    print(nombre,tipo_documento,numero,descripcion,empresa,sep='\n')
    
    uuid_empresa = empresa[-36:]
    objeto_uuid = uuid.UUID(uuid_empresa)

    
    
    empresa=Empresa.objects.filter(codigo=objeto_uuid).first()
    usuario = User.objects.filter(id = request.user.id).first()
    tipo_docu = models.TipoDocumento.objects.filter(tipo_documento=tipo_documento).first()

    models.Persona.objects.create(
        usuario= usuario,
        nombre=nombre,
        empresa=empresa,
        tipodocumento = tipo_docu,
        numero=numero,
        )

    return redirect('/home/')


def view_pesonas(request):

    context = {
        'personas' :models.Persona.objects.filter().all()
    }
    
    return render(request, 'view_persona.html', context)


def delete_persona(request, code):
    persona =  models.Persona.objects.filter(codigo=code).first() 

    persona.delete()

    return redirect('/home/')

    
def view_actualizar (request, code):

    context ={
    'persona' : models.Persona.objects.filter(codigo=code).first()
    } 
  

    return render(request,'actualizar_persona.html', context)
    
    

    