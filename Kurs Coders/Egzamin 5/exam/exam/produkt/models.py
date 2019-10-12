from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField()
    available = models.BooleanField(default=True)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=64)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

