
from django.urls import path
from . import views



urlpatterns = [
   path('registrar/', views.viewcreate_vehiculo, name='create_vehiculoview' ),
   path('listado-vehiculos/', views.view_vehiculo, name='vehiculos' ),
   path('registrar/vehiculo', views.create_vehiculo,name='create_vehiculo'),
   path('eliminar/vehiculo/<uuid:code>', views.delete_vehiculo, name='delete_vehiculo'),
   path('actualizar/<uuid:code>', views.view_actualizar, name='actualizar_vehiculo_from')

    
] 