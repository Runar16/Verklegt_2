from django.contrib import admin
from .models import PropertyType, PropertyZip, Property, PropertyImage, Order

admin.site.register(PropertyType)
admin.site.register(PropertyZip)
admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(Order)
