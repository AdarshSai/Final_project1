from django.db import models

# Create your models here.
from django.db import models
import datetime
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils import timezone

# Create your models here.


class Patient(models.Model):
    CATEGORY = [('W', 'Worst'),
                    ('G', 'Good'),
                    ('B', 'Better- Slowly Recovering'),
                    ('V', 'Vulnerable')]
    CARE=[('I','Intensive Care'),('B','Behavioural Care'),('P','Palliative Care'),('O','Ordinary Care'),('S','Special Care')]
    name = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY, max_length=300, default="")
    age=models.IntegerField()
    address=models.CharField(max_length=1000)
    severity=models.CharField(max_length=1000)
    issues=models.CharField(max_length=1000)
    date_admitted=models.DateField()
    care_provided=models.CharField(choices=CARE,default="",max_length=1000)
    care_needed=models.CharField(max_length=1000)
    health_level=models.CharField(max_length=1000)
class Volunteer(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    proof=models.CharField(max_length=200)
    lisences_hold=models.CharField(max_length=200)
    verfication_status=models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    available_date=models.DateField()
    services=models.CharField(max_length=1000)
class Nurse(models.Model):
    name=models.CharField(max_length=1000)
    age=models.IntegerField()
    years_of_experience=models.DecimalField(decimal_places=2,max_digits=10)
    address=models.CharField(max_length=1000)
    specialisation=models.CharField(max_length=200)
    availability=models.DateTimeField()
