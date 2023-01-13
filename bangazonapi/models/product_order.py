from django.db import models
from .product import Product
from .order import Order

class ProductOrder(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  quantity = models.IntegerField()
