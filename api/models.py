from django.db import models

class CarModels(models.Model):
    image = models.ImageField('изображение', upload_to='cars/')
    name = models.CharField('модель',max_length=100)
    fuel = models.CharField('топливо',max_length=100)
    price = models.CharField('цена',max_length=100)



    def __str__(self):
        return self.name





