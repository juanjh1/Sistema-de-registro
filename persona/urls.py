
from django.urls import path

from . import views

urlpatterns = [
  path('registrar/', views.view_registrar, name='viewregister_persona'),
  path('registrar/usuario', views.registar, name='registrar_persona'),
  path('listado-personas/', views.view_pesonas, name='view_personas'),
  path('eliminar/<uuid:code>', views.delete_persona, name='delete_persona'),
  path('actualizar/<uuid:code>/form', views.view_actualizar, name='view_actualizar_persona'),
   path('actualizar/<uuid:code>', views.view_actualizar, name='actualizar_persona')
]