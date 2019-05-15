from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from property.models import Property, PropertyZip, PropertyType, PropertyImage
from realtor.forms.realtor_forms import NewProperty, ImageForm
from realtor.models import Realtor


def index(request):
    context = {'realtors': Realtor.objects.filter().select_related()}
    return render(request, 'realtor/realtor.html', context)


def get_realtor_by_id(request, id):
    return render(request, 'realtor/details.html', {
        'realtor': get_object_or_404(Realtor, pk=id),
        'properties': Property.objects.filter(realtor_id__exact=id)
    })


def add_property(request):
    ImageFormSet = modelformset_factory(PropertyImage,
                                        form=ImageForm, extra=3)
    if request.method == 'POST':
        property_form = NewProperty(data=request.POST)
        image_form = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
        if property_form.is_valid:
            property_form.save()
            return redirect('add_property')
    else:
        property_form = NewProperty()
        image_form = ImageFormSet(queryset=PropertyImage.objects.none())
    return render(request, 'realtor/add_property.html', {
        'property_form': property_form,
        'image_form': image_form
    })
