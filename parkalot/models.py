import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


# Customer model
class Customer(models.Model):
    carRegistrationNumber = models.CharField(max_length=7)
    # return a string representation
    def __str__(self):
        return self.carRegistrationNumber

# Parking model
# When a customer parks, a parking is created
class Parking(models.Model):
    # every parking has a customer tied to it
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(blank=True, null=True)

    # return time parked
    def get_parking_length(self):
        return (self.endDate - self.startDate)
