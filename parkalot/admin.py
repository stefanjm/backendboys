from django.contrib import admin
from .models import Customer
from .models import Parking
# Register your models here.

# add an admin interface for Customer model
admin.site.register(Customer)

# add an admin interface for Parking model
admin.site.register(Parking)