from django.forms import ModelForm, widgets
from user.models import Profile
from django.contrib.auth.models import User

#goat
class ContactInfoUser(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'password', 'last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'user_permissions', 'groups', 'username']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'})
        }


class ContactInfoProfile(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'profile_picture']
        widgets = {
            'phone_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'ssn': widgets.TextInput(attrs={'class': 'form-control'})
        }
