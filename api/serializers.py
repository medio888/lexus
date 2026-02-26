from rest_framework import serializers
from .models import Footer, Products, Category, SubCategory, Footer, Division


class SubCategorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = SubCategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'sub_categories')
        

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        
        
class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ('departement',)  
        

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'         
        
        
                     