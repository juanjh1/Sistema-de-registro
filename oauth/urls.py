from django.contrib import admin
from django.urls import path
from .  import views


urlpatterns = [
    
    path("register/", views.view_register, name='view_register'),
    path("register/user", views.register, name='register'),
    path("login/", views.view_login, name='view_login'),
    path("login/user", views.login_def, name='login'),
    path("logout/",views.logout_def, name='logout'),
    path("recovery/", views.view_forgotpassword, name= 'view_recoverypass')

] 