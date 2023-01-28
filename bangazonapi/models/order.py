from django.db import models
from .payment_type import PaymentType
from .customer import Customer
from django.forms.models import model_to_dict

class Order(models.Model):
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_placed = models.DateTimeField()

    @property
    def product_orders_on_order(self):
        return self.__product_orders_on_order
    
    @product_orders_on_order.setter
    def product_orders_on_order(self, value):
        self.__product_orders_on_order = value
