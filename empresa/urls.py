from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('registrar/', views.createview_empresas, name='form_empresa'),
    path('listado-empresas/', views.view_empresas, name='view_empresa'),
    path('registrar/empresa', views.create_empresa, name='empresa_create'),
    path('eliminar/<uuid:code>/', views.delete_empresa, name='empresa_eliminar'),
    path('actualizar/<uuid:code>/', views.actualizar, name='empresa_acutalizar')

] 