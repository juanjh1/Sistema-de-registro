from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/",views.view_clinte, name='view_cliente'),
    path("profile/<int:id>", views.profile, name="profile")
   
    
] 