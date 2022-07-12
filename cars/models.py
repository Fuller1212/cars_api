from django.db import models
from django.forms import CharField

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=255)
    model = CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)