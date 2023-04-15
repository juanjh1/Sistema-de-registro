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
