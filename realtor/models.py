from django.contrib.auth.models import User
from django.db import models


class Realtor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.CharField(max_length=999, blank=True)
    license_number = models.IntegerField(blank=True)