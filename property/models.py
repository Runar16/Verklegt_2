from django.db import models
from django.contrib.auth.models import User
from realtor.models import Realtor


class PropertyType(models.Model):
    type = models.CharField(max_length=100, primary_key=True)

    def get_type(self):
        return "%s" % self.type


class PropertyZip(models.Model):
    zip = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100)

    def get_city(self):
        return "%s" % self.city

    def get_zip(self):
        return "%s" % self.zip


class Property(models.Model):
    street_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=10)
    property_description = models.CharField(max_length=2000)
    zip = models.ForeignKey(PropertyZip, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, default='Iceland')
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    size = models.IntegerField()
    rooms = models.IntegerField(blank=True)
    price = models.FloatField()
    is_active = models.BooleanField()
    realtor = models.ForeignKey(Realtor, default=Realtor.DEFAULT_REALTOR, on_delete=models.SET_DEFAULT)


class PropertyImage(models.Model):
    image = models.CharField(max_length=999)
    image_tag = models.CharField(max_length=999, blank=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


class Order(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    sold_property = models.ForeignKey(Property, null=True, on_delete=models.SET_NULL)
    buyer_ssn = models.CharField(max_length=10)
    sold_street_name = models.CharField(max_length=255)
    sold_street_number = models.CharField(max_length=10)
    realtor_licence_num = models.IntegerField(blank=True)
    sold_zip = models.CharField(max_length=10)
    sale_date = models.DateField(auto_now_add=True)
