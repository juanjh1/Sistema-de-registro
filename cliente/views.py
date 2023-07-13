from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models


def index(request):
    return redirect('/auth/login/')


@login_required
def view_cliente(request):
    info_usuario = models.InformacionUsuario.objects.filter(user=request.user.id).first()
    user = User.objects.get(id=request.user.id)

    if info_usuario is None:
        models.InformacionUsuario.objects.create(user=user)

    context = {
        'user': request.user,
        'info_usuario': models.InformacionUsuario.objects.filter(user=request.user.id).first()
    }

    return render(request, "clienteview.html", context)


@login_required
def profile(request, id):
    usuario = User.objects.get(id=id)
    info_usuario = models.InformacionUsuario.objects.filter(user=id).first()

    context = {
        'usuario': usuario,
        'info_usuario': info_usuario
    }
    return render(request, 'profile.html', context)


@login_required
def informacion_usuario_view(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        foto = request.FILES.get('foto')
        numerotelefonico = request.POST.get('numerotelefonico')
        genero = request.POST.get('genero')
        direccion = request.POST.get('direccion')
        fechanacimiento = request.POST.get('fechanacimiento')

        informacion_usuario = models.InformacionUsuario.objects.create(
            foto=foto,
            numerotelefonico=numerotelefonico,
            genero=genero,
            direccion=direccion,
            fechanacimiento=fechanacimiento,
            user=user
        )
        print(informacion_usuario)

        return redirect('/home/')  # Redirige a la página principal de tu app

    return render(request, 'informacion_usuario.html')


def search(request):
    name = request.GET['search']
    user = User.objects.filter(username=name).first()

    if user is not None:
        return redirect(f'/profile/{user.id}')
    return redirect('/home/')