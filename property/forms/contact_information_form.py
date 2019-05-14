from django.forms import ModelForm, widgets

from property.models import Order
from user.models import Profile, Cart
from django.contrib.auth.models import User
from django import forms


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
    card_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Card number'}))
    expiration_month = forms.ChoiceField(choices=MONTHS, label="Expiration month", initial='', widget=forms.Select())
    expiration_year = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '2019'}), max_length=4)
    cvv = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'CVV'}), max_length=3)


class CartForm(ModelForm):
    class Meta:
        model = Cart
        exclude = ['id', 'property', 'user']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = [
                    'id',
                    'buyer_ssn',
                    'sold_street_name',
                    'sold_street_number',
                    'realtor_licence_num',
                    'sold_zip', 'sale_date',
                    'customer',
                    'sold_property'
                   ]
