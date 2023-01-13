from django.db import models
from .customer import Customer

class PaymentType(models.Model):
    label = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
