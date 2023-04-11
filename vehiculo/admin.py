from django.contrib import admin
from vehiculo import models

# Register your models here.
admin.site.register(models.Vehiculo)
admin.site.register(models.Vehiculo_Estado)
admin.site.register(models.Estado)
admin.site.register(models.Marca)
admin.site.register(models.Modelo)
 