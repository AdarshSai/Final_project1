"""Palleative_Care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path(r'', TemplateView.as_view(template_name='Palleative_Care/base.html'), name='base'),
    path(r'nurse', TemplateView.as_view(template_name='Palleative_Care/Nurse.html'), name='nurse'),
    path(r'patient', TemplateView.as_view(template_name='Palleative_Care/Patient.html'), name='patient'),
    path(r'volunteer', TemplateView.as_view(template_name='Palleative_Care/Volunteer.html'), name='volunteer'),
    path(r'admin', TemplateView.as_view(template_name='Palleative_Care/Admin.html'), name='admin'),
    path(r'chat_script',TemplateView.as_view(template_name='Palleative_Care/chat_script.html'),name='chat_script'),

]
