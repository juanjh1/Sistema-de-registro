
from django.urls import path
from . import views



urlpatterns = [
   path('listado-vehiculos/', views.view_vehiculo, name='vehiculos' ),
   path('registrar/vehiculo', views.create_vehiculo,name='create_vehiculo'),
   path('eliminar/vehiculo/<uuid:code>', views.delete_vehiculo, name='delete_vehiculo'),
   path('actualizar/<uuid:code>/form', views.view_actualizar, name='actualizar_vehiculo_from'),
   path('actualizar/<uuid:code>', views.actualizar, name='actualizar_vehiculo'),
   path('detail/<uuid:code>', views.vehiculo_detail, name='vehiculo_detail')

    
] 