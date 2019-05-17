from django.forms import ModelForm, widgets
from property.models import Property, PropertyImage
from django import forms


class NewProperty(ModelForm):
    class Meta:
        model = Property
        exclude = ['id', 'is_active', 'realtor']
        widgets = {
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'property_description': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
        }


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = PropertyImage
        fields = ('image', )
