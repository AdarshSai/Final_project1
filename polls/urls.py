
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    path(r'', TemplateView.as_view(template_name='Palleative_Care/base.html'), name='base'),
    path(r'nurse',TemplateView.as_view(template_name='Palleative_Care/Nurse.html'),name='nurse'),
    path(r'patient',TemplateView.as_view(template_name='Palleative_Care/Patient.html'),name='patient'),
    path(r'volunteer',TemplateView.as_view(template_name='Palleative_Care/Volunteer.html'),name='volunteer'),
    path(r'admin',TemplateView.as_view(template_name='Palleative_Care/Admin.html'),name='admin'),
    path(r'chat_script',TemplateView.as_view(template_name='Palleative_Care/chat_script.html'),name='chat_script'),]