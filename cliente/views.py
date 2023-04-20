from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import  models
# Create your views here.


def index(request):

    context = {

        'user': request.user
     
    }
    
    return render(request, "index.html", context)

@login_required
def view_clinte (request):

    info_usario = models.InformacionUsuario.objects.filter(user=request.user.id).first()
    user = User.objects.filter(id=request.user.id).first(  )

    
    
    if info_usario is None:
        
       models.InformacionUsuario.objects.create(
            user = user
        )
       pass

    context = {

        'user': request.user
     
    }
    
    return  render(request,"clienteview.html", context)

@login_required
def profile (request, id): 
    
    
    

    context = {

    'usuario': User.objects.filter(id=id).first(),
    'info_usuario': models.InformacionUsuario.objects.filter(user=request.user.id).first()

    }
    return render( request, 'profile.html', context)