from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Patient,Volunteer,Nurse

admin.site.register(Patient)
admin.site.register(Volunteer)
admin.site.register(Nurse)
