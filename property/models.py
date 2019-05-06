from django.db import models

# Create your models here.
class Property(models.model):
    street_name = models.CharField(max_length=255)
    street_number = models.IntegerField()
    property_description = models.CharField(2000)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    size = models.IntegerField()
    rooms = models.IntegerField()
    price = models.FloatField()

class PropertyImage(models.model):
    image = models.CharField(max_length=999)
    property = models.ForeignKey(Property, on_delete=models.CASCADE())