# mysite/serializers.py
from rest_framework import serializers
from .model import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'carmodel']
