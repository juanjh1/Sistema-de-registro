from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your models here.

class InformacionUsuario (models.Model):
    foto = models.ImageField( upload_to="perfil/", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    slug = models.SlugField(null=True)
    phone_number = models.CharField( max_length=50, null=True)
    genero = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=60, null=True)
    born_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instagram = models.URLField(null=None)
    facebook = models.URLField(null=None)
    twiter = models.URLField(null=None)

    @staticmethod
    def user_info_by_id(id): 
        InformacionUsuario.objects.get_or_404(user__id=id).first()