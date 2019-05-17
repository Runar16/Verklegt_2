from django.contrib.auth.models import User
from django.db import models


class Realtor(models.Model):
    DEFAULT_REALTOR = 25
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.IntegerField(blank=True)

    def get_licence(self):
        return "%s" % self.license_number

    def __str__(self):
        return str(self.user.first_name + ' ' + self.user.last_name)
