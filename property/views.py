from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.db import IntegrityError
from property.forms.contact_information_form import ContactInfoUser, ContactInfoProfile, PaymentInfo, CartForm
from property.models import Property, PropertyZip, PropertyType
from user.models import History, Cart


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
    if request.user.is_authenticated:
        context = {'properties': Property.objects.all().order_by('price'),
            'zips': PropertyZip.objects.all().order_by('zip'),
            'types': PropertyType.objects.all().order_by('type'),
            'history': History.objects.filter(user=request.user).order_by('-datetime_stamp')
               }
    else:
        context = {'properties': Property.objects.all().order_by('price'),
                   'zips': PropertyZip.objects.all().order_by('zip'),
                   'types': PropertyType.objects.all().order_by('type'),
                   }
    return render(request, 'property/frontpage.html', context)


def get_property_by_id(request, id):
    if request.user.is_authenticated:
        current_user = request.user.id
        if request.method == 'POST':
            try:
                Cart.objects.create(property_id=id, user_id=current_user)
            except IntegrityError:
                pass
        timestamp = datetime.datetime.now()
        try:
            History.objects.create(property_id=id, user_id=current_user, datetime_stamp=timestamp)
        except IntegrityError:
            existing_history_obj = History.objects.get(property_id=id, user_id=current_user)
            History.objects.filter(pk=existing_history_obj.id).update(datetime_stamp=timestamp)
    return render(request, 'property/details.html', {
        'property': get_object_or_404(Property, pk=id),
        'cart_form': CartForm()
    })

def get_property_by_realtor_id(request, id):
    return render(request, 'realtor/details.html', {
        'properties': Property.objects.all().filter(realtor_id=id)
    })


def payment_info(request):
    return render(request, 'property/payment_info.html', {
        'payment_form': PaymentInfo(),
    })


def review_purchase(request):
    pay_info = PaymentInfo(request.POST)
    return render(request, 'property/review_purchase.html', {"pay_info": pay_info})


def about_us(request):
    return render(request, 'about_us.html')


@login_required
@transaction.atomic
def contact_info(request):
    if request.method == 'POST':
        user_form = ContactInfoUser(request.POST, instance=request.user)
        profile_form = ContactInfoProfile(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('payment_info')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = ContactInfoUser(instance=request.user)
        profile_form = ContactInfoProfile(instance=request.user.profile)
    return render(request, 'property/contact_info.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
