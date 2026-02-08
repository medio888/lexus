from rest_framework import serializers
from .models import CarModels


class CarModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModels
        fields = '__all__'