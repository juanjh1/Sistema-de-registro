from django.shortcuts import render,redirect
from  django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.utils import timezone

# Create your views here.

def view_register(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        return render (request,"registro.html")


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if 6 <= len(password) <= 10:
            valid_username = User.objects.filter(username=username).first()
            valid_email = User.objects.filter(email=email).first()

            if valid_email is None and valid_username is None:
                password_enc = make_password(password)
                User.objects.create(
                    first_name=name, 
                    last_name=lastname, 
                    username=username, 
                    email=email, 
                    password=password_enc, 
                    is_staff=False
                )
                messages.success(request, 'User created')
                
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/home/')
                else:
                    pass
            else:       
                if valid_username is not None:
                    messages.error(request, 'Usuario en uso')
                elif valid_email is not None:
                    messages.error(request, 'Correo en uso')
                else:
                    messages.error(request, 'Error inesperado')
    return render(request, 'registro.html')

def view_login(request): 
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        return render(request, "login.html")
    

def login_def (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Usuario auntenticado')

            return redirect('/home/')
        else:
            messages.error(request, 'Error el las credeciales ingresadas')
            
    return redirect('/auth/login/')

@login_required
def logout_def(request):

    logout(request)
    messages.success(request, 'Sesion cerrada correctamente ')
    return redirect('/')

def view_forgotpassword (request): return render(request, 'forgot-password.html')



