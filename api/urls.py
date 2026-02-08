from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CarViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]