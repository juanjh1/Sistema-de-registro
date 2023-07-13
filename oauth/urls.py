from django.contrib import admin
from django.urls import path
from .  import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path("register/", views.view_register, name='view_register'),
    path("register/user", views.register, name='register'),
    path("login/", views.view_login, name='view_login'),
    path("login/user", views.login_def, name='login'),
    path("logout/",views.logout_def, name='logout'),
    path("recovery/", views.view_forgotpassword, name= 'view_recoverypass'),
    path('reset-password/', auth_views.PasswordResetView.as_view(
        template_name='forgot-password.html',
        email_template_name='password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt'
    ), name='password_reset'),
     path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),
     path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
] 