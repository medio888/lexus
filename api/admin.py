from django.contrib import admin
from .models import Products, Category, SubCategory, Footer, Division


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):  
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SubCategory)        
class SubCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    pass


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    pass



