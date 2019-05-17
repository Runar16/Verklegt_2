from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from property.models import Property


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profileimage/', blank=True, default='profileimage/twitter_eggandgumdrop.0.jpg')
    street_name = models.CharField(max_length=255, blank=True)
    street_number = models.CharField(max_length=10, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    ssn = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user.first_name + ' ' + self.user.last_name)


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    datetime_stamp = models.DateTimeField()

    class Meta:
        unique_together = (("user", "property"),)

    def __str__(self):
        return str(
            'User: ' +
            self.user.first_name +
            ' ' +
            self.user.last_name +
            ' Property: ' +
            self.property.street_name +
            ' ' +
            self.property.street_number
        )


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "property"),)

    def __str__(self):
        return str(
            'User: ' +
            self.user.first_name +
            ' ' +
            self.user.last_name +
            ' Property: ' +
            self.property.street_name +
            ' ' +
            self.property.street_number
        )


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "property"),)

    def __str__(self):
        return str(
            'User: ' +
            self.user.first_name +
            ' ' +
            self.user.last_name +
            ' Property: ' +
            self.property.street_name +
            ' ' +
            self.property.street_number
        )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
