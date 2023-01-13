from django.db import models

class ProductType(models.Model):
  label = models.CharField(max_length=50)
