from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def view_empresas():


    pass


def createview_empresas(request):

    return render(request, 'reg_empresa.html')
