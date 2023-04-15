from django.shortcuts import render
from . import models

# Create your views here.


def  viewcreate_vehiculo(request): return render(request, 'reg_vehiculo.html')


def  view_vehiculo(request):
 
 context = {
  
   'vehiculo':models.Vehiculo.objects.filter().all()
  
 }
 return render(request, 'view_vehiculo.html', context)