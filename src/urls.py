"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import edit, dashboard, register
from django import reverse_lazy
from django.contrib.auth.views import (LoginView,LogoutView,PasswordResetDoneView,PasswordResetView,PasswordResetCompleteView,
                                PasswordResetConfirmView,PasswordChangeView,PasswordChangeDoneView,PasswordResetDoneView)

app_name = 'authapp'                                

urlpatterns = [
    path('register/', register, name = 'register'),
    path('edit/', edit, name = 'edit'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('',LoginView.as_view(template_name = 'registration/login.html'),name = 'login'),
    path('logout/',LogoutView.as_view(template_name = 'authapp/logged_out.html'),name = 'logout'),
    path('password_change/',PasswordChangeView.as_view(template_name = 'authapp/password_change_form.html'),name = 'password_change'),
    path('password_change/Done/',PasswordChangeDoneView.as_view(template_name = 'authapp/password_change_done.html'),name = 'password_change_done'),
    path('password_reset/',PasswordResetView.as_view(template_name = 'authapp/password_reset_form.html',email_template_name ='authapp/password_reset_email.html',
    success_url = reverse_lazy('authapp:password_reset_done')),name = 'password_reset'),
    path('password_reset/done/',PasswordResetDoneView.as_view(template_name = 'authapp/password_reset_done.html'),name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name = 'authapp/password_reset_confirm.html',success_url = reverse_lazy('authapp:login')),name = 'password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name = 'authapp/password_reset_complete.html'),name = 'password_reset_complete'),

    #path('admin/', admin.site.urls),
]
