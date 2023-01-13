from django.db import models

class Customer(models.Model):
    uid = models.CharField(max_length=50)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_registered = models.DateField()
    bio = models.CharField(max_length=400)
    image = models.CharField(max_length=200)
