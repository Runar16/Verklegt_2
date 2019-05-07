from django.db import models
from django.contrib.auth.models import User
from property.models import Property


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.CharField(max_length=999, blank=True)
    street_name = models.CharField(max_length=255, blank=True)
    street_number = models.CharField(max_length=10, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    ssn = models.CharField(max_length=10, blank=True)


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
