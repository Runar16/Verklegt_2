from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from property.models import Property, PropertyZip, PropertyType


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        try:
            zip_filter = request.GET['zip_filter']
        except KeyError:
            zip_filter = ""
        try:
            type_filter = request.GET['type_filter']
        except KeyError:
            type_filter = ""
        filtered_properties = [{
            'id': x.id,
            'street_name': x.street_name,
            'street_number': x.street_number,
            'property_description': x.property_description,
            'zip': x.zip.get_zip(),
            'city': x.zip.get_city(),
            'country': x.country,
            'type': x.type.get_type(),
            'size': x.size,
            'rooms': x.rooms,
            'price': x.price,
            'is_active': x.is_active,
            'first_image': x.propertyimage_set.first().image
        }for x in Property.objects.filter(street_name__icontains=search_filter,
                                          zip__zip__contains=str(zip_filter),
                                          type__type__contains=type_filter
                                          )
        ]
        return JsonResponse({'data': filtered_properties})

    context = {'properties': Property.objects.all().order_by('price'),
               'zips': PropertyZip.objects.all().order_by('zip'),
               'types': PropertyType.objects.all().order_by('type')
               }
    return render(request, 'property/frontpage.html', context)


def get_property_by_id(request, id):
    return render(request, 'property/details.html', {
        'property': get_object_or_404(Property, pk=id)
    })

def customer_info(request):
    return render(request, 'property/customer_info.html')

def payment_info(request):
    return render(request, 'property/payment_info.html')

def about_us(request):
    return render(request, 'about_us.html')