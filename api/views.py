from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, CarModels
from .serializers import CategorySerializer, CarSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = CarModels.objects.all()
    serializer_class = CarSerializer
