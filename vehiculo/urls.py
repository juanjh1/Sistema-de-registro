
from django.urls import path
from . import views



urlpatterns = [
   path('registrar/', views.viewcreate_vehiculo, name='create_vehiculo' ),
   path('listado-vehiculos/', views.view_vehiculo, name='vehiculos' )

    
] 