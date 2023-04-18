
from django.urls import path

from . import views

urlpatterns = [
  path('registrar/', views.view_registrar, name='viewregister_persona'),
  path('registrar/usuario', views.registar, name='registrar_persona'),
  path('listado-personas/', views.view_pesonas, name='view_personas')
]