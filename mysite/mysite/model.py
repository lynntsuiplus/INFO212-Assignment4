# mysite/models.py
from django.db import models
from django.core.validators import *


class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(120)])
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.age}, {self.address}'


class Car(models.Model):
    class CarStatus(models.TextChoices):
        AVAILABLE = 'A', 'Available'
        BOOKED = 'B', 'Booked'
        RENTED = 'R', 'Rented'
        DAMAGED = 'D', 'Damaged'
    make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    year = models.PositiveIntegerField()
    location = models.CharField(max_length=50)
    status = models.CharField(
        max_length=1,
        choices=CarStatus.choices,
        default=CarStatus.AVAILABLE
    )

    def __str__(self):
        return f'{self.make}, {self.car_model}, {self.year}, {self.location}'

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.address}, {self.branch}'


