from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from property.models import Property


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        properties = [{
            'id': x.id,
            'street_name': x.street_name,
            'street_number': x.street_number,
            'property_description': x.property_description,
            'zip_id': x.zip_id_set.first().zip,
            'city': x.zip_id_set.first().city,
            'country': x.country,
            'type': x.type_id_set.first().type,
            'size': x.size,
            'rooms': x.rooms,
            'price': x.price,
            'is_active': x.is_active,
            'first_image': x.propertyimage_set.first().image
        }for x in Property.objects.filter(street_name__icontains=search_filter)]
        return JsonResponse({'data': properties})
    context = {'properties': Property.objects.all().order_by('price')}
    return render(request, 'property/frontpage.html', context)


def get_property_by_id(request, id):
    return render(request, 'property/details.html', {
        'property': get_object_or_404(Property, pk=id)
    })

def customer_info(request):
    return render(request, 'property/customer_info.html')

def payment_info(request):
    return render(request, 'property/payment_info.html')
