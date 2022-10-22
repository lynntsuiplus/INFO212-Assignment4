# mysite/models.py
from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)


def __str__(self):
    return self.make + ' ' + + self.carmodel
# make and model are attributes where we can store strings.
# The __str__ method just tells Django what to print when it needs to
# print out an instance of the Car model.
