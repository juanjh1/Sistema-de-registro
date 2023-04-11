from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Empresa)
admin.site.register(models.Federacion)
admin.site.register(models.Licencia)
admin.site.register(models.Paradero)
admin.site.register(models.Empresa_paradero)