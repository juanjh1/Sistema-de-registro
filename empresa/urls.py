from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('registrar/', views.create_empresa, name='create_empresa'),
    path('listado-empresas/', views.view_empresas, name='view_empresa'),
    path('eliminar/<uuid:code>/', views.delete_empresa, name='eliminar_empresa'),
    path('actualizar/<uuid:code>/', views.actualizar_empresa, name='actualizar_empresa'),
    path('registrar/liciencia/<uuid:code>/', views.create_licencia, name='create_licencia'),
    path('regitrar/paradero', views.create_paradero, name='create_paradero'),
    path('paradero', views.view_paradero, name='paraderos'),
    path('eliminar/paradero/<uuid:code>/', views.delete_paradero, name='eliminar_paradero'),
     path('actualizar/paradero/<uuid:code>/', views.actualizar_paradero, name='actualizar_paradero'),
    path('detail/empresa/<uuid:codigo>/', views.empresa_detail, name='detail_empresa' ),
    path('registar/paradero_empresa/<uuid:code>/ ', views.paradero_empresa, name='paradero_empresa'),
    path( 'eliminar/<uuid:code>/paradero/', views.eliminar_paradero_empresa, name='eliminar_paradero_empresa')
] 