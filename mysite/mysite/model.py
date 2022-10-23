# mysite/models.py
from django.db import models
from django.core.validators import *


class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.make}, {self.carmodel}'


class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(120)])
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.age}, {self.address}'
