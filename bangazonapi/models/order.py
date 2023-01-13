from django.db import models
from .payment_type import PaymentType

class Order(models.Model):
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    date_placed = models.DateTimeField()
