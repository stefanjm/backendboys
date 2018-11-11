from django.db import models

# Create your models here.


# Customer model
class Customer(models.Model):
    carRegistrationNumber = models.CharField(max_length=7)

# Parking model
class Parking():
    carRegistrationNumber = models.CharField(max_length=7)
    startDate = models.DateTimeField(auto_now=True)
    endDate = models.DateTimeField()
