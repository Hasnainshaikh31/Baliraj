from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Supplier(models.Model):
    firstName = models.CharField(max_length=150)
    middleName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    phoneNumber = models.DecimalField(max_digits = 10, decimal_places = 0, blank=True)
    mobileNumber = models.DecimalField(max_digits = 10, decimal_places = 0, blank = False)
    email = models.EmailField(max_length = 255, blank = False)
    emailOptional = models.EmailField(max_length = 255, blank = True)
    address = models.TextField(blank = False, null = False)
    areaStreet = models.TextField(blank = False, null = False)
    city = models.CharField(max_length = 255)
    district = models.CharField(max_length = 255)
    taluka = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    pinCode = models.DecimalField(max_digits = 6, decimal_places = 0)
    # organizationName 
    # designation
