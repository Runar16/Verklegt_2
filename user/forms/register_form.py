from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterProfileForm(UserCreationForm):
    zip = forms.IntegerField()
    city = forms.CharField()
    phone_number = forms.IntegerField()
    street_name = forms.CharField()
    street_number = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username',
                  'zip',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'email',
                  'city',
                  'phone_number',
                  'street_number',
                  'street_name'
                  )
