from django.shortcuts import render
from rest_framework import viewsets
from .models import CarModels
from .serializers import CarModelsSerializer

class CarModelsViewSet(viewsets.ModelViewSet):
    queryset = CarModels.objects.all()
    serializer_class = CarModelsSerializer
