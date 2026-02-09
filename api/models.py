from django.db import models



class Products(models.Model):
    model = models.CharField(verbose_name='Model', max_length=255)
    price = models.DecimalField(verbose_name='Price', max_digits=14, decimal_places=2)
    vin = models.CharField(verbose_name='VIN-code', max_length=255, unique=True)
    amount = models.IntegerField(verbose_name='Amount', default=0)
    fuel = models.CharField(verbose_name='Fuel', max_length=255)
    gearbox = models.CharField(verbose_name='Gearbox', max_length=255)
    year = models.IntegerField(verbose_name='Year')
    color = models.CharField(verbose_name='Color', max_length=255)
    car_body = models.CharField(verbose_name='Car Body', max_length=255)
    drive = models.CharField(verbose_name='Drive', max_length=255)
    volume = models.DecimalField(verbose_name='Volume', max_digits=4, decimal_places=1)


    def __str__(self):
        return self.model
    

class Category(models.Model):
    name = models.CharField(verbose_name='Category', max_length=255)

    def __str__(self):
        return self.name    
    

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    model = models.CharField(verbose_name='Model', max_length=255)
    icon = models.ImageField(upload_to='subcategory_icons/', null=True, blank=True)

    def __str__(self):
        return self.model

    


