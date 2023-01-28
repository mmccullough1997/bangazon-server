from django.db import models
from .product import Product
from .order import Order
from .customer import Customer
from django.forms.models import model_to_dict

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()

    @property
    def subtotal(self):
        return self.__subtotal
    
    @subtotal.setter
    def subtotal(self, value):
        self.__subtotal = value
