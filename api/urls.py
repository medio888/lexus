from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarModelsViewSet

router = DefaultRouter()
router.register('model', CarModelsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
