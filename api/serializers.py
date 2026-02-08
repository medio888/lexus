from rest_framework import serializers
from .models import Category, CarModels


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModels
        fields = '__all__'