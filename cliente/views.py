from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import  models
# Create your views here.


def index(request):

    return redirect('/auth/login/')

@login_required
def view_clinte (request):

    info_usario = models.InformacionUsuario.objects.filter(user=request.user.id).first()
    user = User.objects.filter(id=request.user.id).first(  )

    
    
    if info_usario is None:
        
       models.InformacionUsuario.objects.create(
            user = user
        )
       
   
    context = {

        'user': request.user,
        'info_usuario': models.InformacionUsuario.objects.filter(user=request.user.id).first()
     
    }
    
    return  render(request,"clienteview.html", context)

@login_required
def profile (request, id): 
    
    
    

    context = {

    'usuario': User.objects.filter(id=id).first(),
    'info_usuario': models.InformacionUsuario.objects.filter(user=request.user.id).first()

    }
    return render( request, 'profile.html', context)

@login_required
def informacion_usuario_view(request,id):
    
    user= User.objects.filter(id=id).first()
    if request.method == 'POST':
        foto = request.FILES.get('foto')
        numerotelefonico = request.POST.get('numerotelefonico')
        genero = request.POST.get('genero')
        direccion = request.POST.get('direccion')
        fechanacimiento = request.POST.get('fechanacimiento')
        user = user

        informacion_usuario = models.InformacionUsuario.objects.create(
            foto=foto,
            numerotelefonico=numerotelefonico,
            genero=genero,
            direccion=direccion,
            fechanacimiento=fechanacimiento,
            user=user
        )
        print(informacion_usuario)

        return redirect('/home/') # Redirige a la página principal de tu app

    return render(request, 'informacion_usuario.html')