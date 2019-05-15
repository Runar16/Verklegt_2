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
        formset = ImageFormSet(request.POST, request.FILES, queryset=PropertyImage.objects.none())
        if property_form.is_valid and formset.is_valid():
            property_form = property_form.save(commit=False)
            property_form.realtor = request.user.realtor
            property_form.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = PropertyImage(property=property_form, image=image, image_tag='BLA')
                photo.save()
            return redirect('add_property')
        else:
            print(property_form.errors, formset.errors)
    else:
        property_form = NewProperty()
        formset = ImageFormSet(queryset=PropertyImage.objects.none())
    return render(request, 'realtor/add_property.html', {
        'property_form': property_form,
        'formset': formset
    })
