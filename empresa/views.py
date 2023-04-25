from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from  django.contrib.auth.models import User
import datetime
import uuid
# Create your views here.

@login_required
def create_empresa(request): 
    
    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        direccion =  request.POST.get('direccion')
        flota =  request.POST.get('flota')
        correo_electronico =  request.POST.get('correo_electronico')
        fecha_resolucion = request.POST.get('fecha_resolucion')
        numero_resolucion =  request.POST.get('numero_resolucion')
        federacion =  request.POST.get('federacion')
        
        
        models.Empresa.objects.create(
           nombre=nombre,
           direccion=direccion,
           flota = flota,
           correo_electronico = correo_electronico,
           numero_resolucion =  numero_resolucion,
           fecha_resolucion=fecha_resolucion,
           usuario_id = request.user.id,
           federacion= federacion
           
            )
        
       
        return redirect('/home/')

    context = {
        'federaciones': models.Federacion.objects.filter()
    }

    return render(request, 'reg_empresa.html', context)

@login_required
def view_empresas(request):
    
    
    
    context = {
    'user': User.objects.filter(id=request.user.id).first(),
    'empresas': models.Empresa.objects.filter().all()
    }
    return render(request, 'view_empresa.html', context)

@login_required
def delete_empresa ( request, code):

    
    empresa =  models.Empresa.objects.filter(codigo=code).first() 

    if empresa.usuario.id == request.user.id:
        empresa.delete()

    return redirect('/home/')

@login_required
def actualizar_empresa (request, code):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        flota = request.POST.get('flota')
        correo_electronico = request.POST.get('correo_electronico')
        fecha_resolucion = request.POST.get('fecha_resolucion')
        numero_resolucion = request.POST.get('numero_resolucion')
        federacion_nombre = request.POST.get('federacion')

        empresa = models.Empresa.objects.filter(codigo=code).first()
        if not empresa:
            return render(request, 'error.html', {'mensaje': 'La empresa no existe.'})

      

        fecha_actualizacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        empresa.nombre = nombre
        empresa.direccion = direccion
        empresa.flota = flota
        empresa.correo_electronico = correo_electronico
        empresa.fecha_resolucion = fecha_resolucion
        empresa.numero_resolucion = numero_resolucion
        empresa.federacion = federacion_nombre
        empresa.fecha_actualizacion = fecha_actualizacion

        empresa.save()

        return redirect('/home/')
    
    empresa = models.Empresa.objects.filter(codigo=code).first()


    context = {
        'empresa': empresa,
        'federaciones': models.Federacion.objects.filter()
    }

    return render(request, 'actualizar_empresa.html',context )

@login_required
def create_licencia (request, code):
   
    if request.method == 'POST':
        empresa =  models.Empresa.objects.filter(codigo=code).first()
        recibo = request.POST.get('Recibo_caja')
        fecha_inicio= request.POST.get('fecha_inicio')
        fecha_final= request.POST.get('fecha_final')
        numero_resolucion = request.POST.get('numero_resolucion')


        models.Licencia.objects.create(

            numero_resolucion = numero_resolucion,
            fecha_inicial = fecha_inicio,
            fecha_final =fecha_final,
            Recibo_caja = recibo,
            empresa =    empresa

        )

        return redirect('/home/')
    context = {
       'empresa': models.Empresa.objects.filter(codigo=code).first()
    }
   
   
    return render(request, 'licencia_form.html', context)


def create_paradero(request):

    if request.method =='POST':
     
        nombre = request.POST.get('nombre')
        fecha_resolucion = request.POST.get('fecha_resolucion')
        numero_resolucion = request.POST.get('numero_resolucion')

        models.Paradero.objects.create(

            nombre = nombre,
            numero_resolucion = numero_resolucion,
            fecha_resolcuion = fecha_resolucion

        )
   
        return redirect('/home/')
      

    return render(request,'paradero/registrar_paradero.html')


    
def view_paradero(request):

     
    context={
     'paraderos': models.Paradero.objects.all()
    }

    return render(request,'paradero/view_paradero.html', context)


@login_required
def delete_paradero(request, code):
    
    paradero = models.Paradero.objects.filter(codigo=code).first()

    paradero.delete()

    return redirect('/home/')

def empresa_detail(request, codigo):

    context = {
         'user': User.objects.filter(id=request.user.id).first(),
         'empresa': models.Empresa.objects.filter(codigo=codigo).first(),
         'paradero_empresa': models.Empresa_paradero.objects.filter(empresa=codigo)
    }
   

    return render(request, 'detail_empresa.html', context)


def paradero_empresa(request, code):
 
    if request.method == 'POST':
        paradero= request.POST.get('paradero')
        
        paradero= uuid.UUID(paradero)

        paradero = models.Paradero.objects.filter(codigo=paradero).first()

        empresa = models.Empresa.objects.filter(codigo=code).first()

        models.Empresa_paradero.objects.create(
            empresa = empresa,
            paradero = paradero
        )

    redirect ('/home/')
        


    context={
     'paraderos': models.Paradero.objects.filter().all(),
     'empresa': models.Empresa.objects.filter(codigo=code).first()

    }



    return render(request,'paradero/paradero_empresa.html', context)
    

def actualizar_paradero(request,code):
    
    context ={

    }

    return render(request,'paradero/actualizar_paradero.html' , context)
