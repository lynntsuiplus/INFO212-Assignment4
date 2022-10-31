# mysite/admin.py
from django.contrib import admin
from .model import *

# Register your models here.
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Employee)

