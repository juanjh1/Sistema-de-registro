from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from  django.contrib.auth.models import User
from cliente.models import InformacionUsuario
import datetime
import uuid
from django.utils import timezone
from django.core.paginator import Paginator
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
        
       
        return redirect('/empresa/listado-empresas/')

    context = {
        'federaciones': models.Federacion.objects.filter()
    }

    return render(request, 'reg_empresa.html', context)

@login_required
def view_empresas(request):
    empresas_list = models.Empresa.objects.filter().all()
    paginator = Paginator(empresas_list, 8)  # Número de elementos por página
    page_number = request.GET.get('page')
    empresas = paginator.get_page(page_number)
    
    context = {
    'user': User.objects.filter(id=request.user.id).first(),
    'empresas': empresas,
    'info_usuario': InformacionUsuario.objects.filter(user=request.user.id).first()
    }
    return render(request, 'view_empresa.html', context)

@login_required
def delete_empresa ( request, code):

    
    empresa =  models.Empresa.objects.filter(codigo=code).first() 

    if empresa.usuario.id == request.user.id:
        empresa.delete()

    return redirect('/empresa/listado-empresas/')

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

        return redirect('/empresa/listado-empresas/')
    
    empresa = models.Empresa.objects.filter(codigo=code).first()


    context = {
        'empresa': empresa,
        'federaciones': models.Federacion.objects.filter()
    }

    return render(request, 'actualizar_empresa.html',context )

@login_required
def create_licencia(request, code):
    if request.method == 'POST':
        empresa = models.Empresa.objects.filter(codigo=code).first()

        recibo = request.POST.get('Recibo_caja')
        archivo = request.POST.get('archivo')
        fecha_inicio_str = request.POST.get('fecha_inicial')
        fecha_final_str = request.POST.get('fecha_final')
        numero_resolucion = request.POST.get('numero_resolucion')

       
        if fecha_inicio_str:
            fecha_inicio = timezone.datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
        else:
            fecha_inicio = None


        if fecha_final_str and fecha_inicio:
            fecha_final = timezone.datetime.strptime(fecha_final_str, "%Y-%m-%d").date()

            if fecha_final <= fecha_inicio:
                context = {
                    'empresa': empresa,
                    'error_message': 'La fecha final debe ser mayor que la fecha inicial.'
                }
                return render(request, 'licencia_form.html', context)

            models.Licencia.objects.create(
                numero_resolucion=numero_resolucion,
                fecha_inicial=fecha_inicio,
                fecha_final=fecha_final,
                Recibo_caja=recibo,
                empresa=empresa,
                pdf=archivo
            )

            return redirect('/empresa/listado-empresas/')
        else:
            context = {
                'empresa': empresa,
                'error_message': 'Falta proporcionar la fecha inicial o final.'
            }
            return render(request, 'licencia_form.html', context)

    context = {
        'empresa': models.Empresa.objects.filter(codigo=code).first()
    }
    return render(request, 'licencia_form.html', context)

@login_required
def create_paradero(request):
    if request.method =='POST':
     
        nombre = request.POST.get('nombre')
        fecha_resolucion = request.POST.get('fecha_resolucion')
        numero_resolucion = request.POST.get('numero_resolucion')
        usuario = User.objects.filter(id=request.user.id).first()

        models.Paradero.objects.create(

            nombre = nombre,
            numero_resolucion = numero_resolucion,
            fecha_resolcuion = fecha_resolucion,
            usuario= usuario

        )
   
        return redirect('/empresa/paradero')
      

    return render(request,'paradero/registrar_paradero.html')


@login_required   
def view_paradero(request):

    paradero_list = models.Paradero.objects.all()
    paginator = Paginator(paradero_list, 8)  # Número de elementos por página
    page_number = request.GET.get('page')
    paradero = paginator.get_page(page_number)
    context={
     'paraderos': paradero
    }

    return render(request,'paradero/view_paradero.html', context)


@login_required
def delete_paradero(request, code):
    
    paradero = models.Paradero.objects.filter(codigo=code).first()

    paradero.delete()

    return redirect('/empresa/paradero')

@login_required
def empresa_detail(request, codigo):

    context = {
         'user': User.objects.filter(id=request.user.id).first(),
         'empresa': models.Empresa.objects.filter(codigo=codigo).first(),
         'paradero_empresa': models.Empresa_paradero.objects.filter(empresa=codigo)
    }

    return render(request, 'detail_empresa.html', context)

@login_required
def paradero_empresa(request, code):
 
    if request.method == 'POST':
        paradero= request.POST.get('paradero')
        
        paradero= uuid.UUID(paradero)

        paradero = models.Paradero.objects.filter(codigo=paradero).first()

        empresa = models.Empresa.objects.filter(codigo=code).first()

        """if models.Empresa_paradero.objects.filter(paradero=paradero).first != None:
            
            return  redirect('/home/')
        """
        models.Empresa_paradero.objects.create(
            empresa = empresa,
            paradero = paradero
        )
        return redirect (f'/empresa/detail/empresa/{code}/')


    context={
     'paraderos': models.Paradero.objects.filter().all(),
     'empresa': models.Empresa.objects.filter(codigo=code).first()

    }

    return render(request,'paradero/paradero_empresa.html', context)
    
@login_required
def actualizar_paradero(request,code):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        fecha_resolucion = request.POST.get('fecha_resolucion')
        numero_resolucion = request.POST.get('numero_resolucion')
        usuario = User.objects.filter(id=request.user.id).first()
        
        fecha_actualizacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(nombre, fecha_resolucion, numero_resolucion, usuario)
    
        paradero = models.Paradero.objects.filter(codigo = code).first()

        paradero.fecha_actualizacion = fecha_actualizacion
        paradero.fecha_resolcuion = fecha_resolucion
        paradero.numero_resolucion = numero_resolucion
        paradero.nombre = nombre
        
        paradero.save()

        return redirect('/empresa/paradero')


    context ={
        'paradero': models.Paradero.objects.filter(codigo=code).first()
    }

    return render(request,'paradero/actualizar_paradero.html' , context)

@login_required
def eliminar_paradero_empresa(request, code):


    paradero_empresa = models.Empresa_paradero.objects.filter(paradero=code).first()
    empresa_code = paradero_empresa.empresa.codigo
    
    paradero_empresa.delete()

    return redirect (f'/empresa/detail/empresa/{empresa_code}/')

def deleate_licencia(request,code ):

    licencia = models.Licencia.objects.filter(codigo=code).first()

    empresa = licencia.empresa.codigo
     
    licencia.delete()

    return redirect (f'/empresa/detail/empresa/{empresa}/')