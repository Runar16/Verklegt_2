from django.forms import ModelForm, widgets
from user.models import Profile
from django.contrib.auth.models import User
from django import forms


class ContactInfoUser(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactInfoUser, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = User
        exclude = [
            'id',
            'password',
            'last_login',
            'is_superuser',
            'is_active',
            'is_staff',
            'date_joined',
            'user_permissions',
            'groups',
            'username'
        ]
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'})
        }


class ContactInfoProfile(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactInfoProfile, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = True
        self.fields['street_name'].required = True
        self.fields['street_number'].required = True
        self.fields['zip'].required = True
        self.fields['city'].required = True
        self.fields['country'].required = True
        self.fields['ssn'].required = True

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
            'ssn': widgets.NumberInput(attrs={'class': 'form-control'})
        }


class PaymentInfo(forms.Form):
    MONTHS = (
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
    )
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full name (on card)'}))
    card_number = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Card number'}))
    expiration_month = forms.ChoiceField(choices=MONTHS, label="Expiration month", initial='', widget=forms.Select())
    expiration_year = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '2019'}), max_length=4)
    cvv = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'CVV'}), max_length=3)
