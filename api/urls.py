from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, FooterViewSet, DivisionViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('subcategory', SubCategoryViewSet)
router.register('footer', FooterViewSet)
router.register('division', DivisionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
