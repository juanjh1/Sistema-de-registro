from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('registrar/', views.createview_empresas, name='form_empresa'),
    path('listado-empresas/', views.view_empresas, name='view_empresa')
] 