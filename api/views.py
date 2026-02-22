from rest_framework import viewsets, mixins
from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer, CategoryDeteilSerializer


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryDeteilSerializer
        return CategorySerializer

class SubCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer   
    
    



