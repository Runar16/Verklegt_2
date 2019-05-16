from django.forms import ModelForm, widgets
from user.models import Profile
from django.contrib.auth.models import User


class RegisterProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'country', 'ssn']

        widgets = {
            'phone_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
        }
