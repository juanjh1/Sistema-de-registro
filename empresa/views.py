from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.


def view_empresas():


    pass


def createview_empresas(request):

    return render(request, 'reg_empresa.html')


def view_empresas(request):
    
    
    
    context = {
    'empresas': models.Empresa.objects.filter().all()
    }
    return render(request, 'view_empresa.html', context)



def view_empresas(request):
    
    
    
    context = {
    'empresas': models.Empresa.objects.filter().all()
    }
    return render(request, 'view_empresa.html', context)



def create_empresa(request):

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        direccion =  request.POST.get('direccion')
        flota =  request.POST.get('flota')
        correo_electronico =  request.POST.get('correo_electronico')
        fecha_resolucion = request.POST.get('fecha_resolucion')
        numero_resolucion =  request.POST.get('numero_resolucion')
        federacion =  request.POST.get('federacion')
        
        

        if models.Federacion.objects.filter(nombre=federacion).first() is None: 
            
            models.Federacion.objects.create(
                nombre=federacion

            )

        federacion = models.Federacion.objects.filter(nombre=federacion).first()

        print(federacion)
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

    
    

def delete_empresa ( request, code):

    
    empresa =  models.Empresa.objects.filter(codigo=code).first() 

    if empresa.usuario.id == request.user.id:
        empresa.delete()

    return redirect('/home/')
       

def view_actualizar(request, code):
    empresa = models.Empresa.objects.filter(codigo=code).first()

    
    federacion_nombre = empresa.federacion

   

     

    

    federacion = models.Federacion.objects.filter(nombre=federacion_nombre).first()
    print(federacion)

    context = {
        'empresa': empresa,
        'federacion': federacion
    }

    return render(request, 'actualizar_empresa.html',context )
