
from django.db import models

# Create your models here.


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
    #TODO add realtor foreign key


class PropertyImage(models.Model):
    image = models.CharField(max_length=999)
<<<<<<< HEAD
    property = models.ForeignKey(Property, on_delete=models.CASCADE())
=======
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

>>>>>>> 63ba87b2387688a79a49291070113b761671ef95
