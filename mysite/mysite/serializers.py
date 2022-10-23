# mysite/serializers.py
from rest_framework import serializers
from .model import Car
from .model import Customer

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'car_model', 'year', 'location', 'status']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'age', 'address']


