from django.db import models
from .customer import Customer
from .product_type import ProductType

class Product(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=400)
    quantity = models.IntegerField()
    image = models.CharField(max_length=200)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
