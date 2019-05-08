from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    street_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=10)
    property_description = models.CharField(max_length=2000)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    type = models.CharField(max_length=100, blank=True)
    size = models.IntegerField()
    rooms = models.IntegerField(blank=True)
    price = models.FloatField()
    is_active = models.BooleanField()
    # TODO add realtor foreign key


class PropertyImage(models.Model):
    image = models.CharField(max_length=999)
    image_tag = models.CharField(max_length=999, blank=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    sold_property = models.ForeignKey(Property, on_delete=None)
