from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/",views.view_cliente, name='view_cliente'),
    path("profile/<int:id>", views.profile, name="profile"),
    path("search", views.search, name='search'),
    path("actualizar/<int:id>", views.informacion_usuario_view, name='actualizar_perfil'),
    path("social/<int:id>", views.socialmedia, name='socialmedia')
] 