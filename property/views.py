from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError
from property.forms.contact_information_form import ContactInfoUser, ContactInfoProfile, PaymentInfo, CartForm, \
    OrderForm
from property.models import Property, PropertyZip, PropertyType, Order
from django.utils import timezone
from user.models import History, Cart, Profile, Favourite
from sys import maxsize
from django.core.serializers import serialize


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
        try:
            price_from = request.GET['priceFrom_filter']
        except KeyError:
            price_from = 0
        try:
            price_to = request.GET['priceTo_filter']
        except KeyError:
            price_to = float("inf")
        try:
            size_from = request.GET['sizeFrom_filter']
        except KeyError:
            size_from = 0
        try:
            size_to = request.GET['sizeTo_filter']
        except KeyError:
            size_to = maxsize
        try:
            rooms_filter = request.GET['rooms_filter']
        except KeyError:
            rooms_filter = ""
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
            'first_image': x.propertyimage_set.first().image.url,
            'image_tag': x.property_description
        }for x in Property.objects.filter(street_name__icontains=search_filter,
                                          zip__zip__contains=str(zip_filter),
                                          type__type__contains=type_filter,
                                          price__gt=price_from-1,
                                          price__lt=price_to-1,
                                          size__gt=size_from-1,
                                          size__lt=size_to-1,
                                          rooms__contains=rooms_filter
                                          )
        ]
        return JsonResponse({'data': filtered_properties})
    context = {'zips': PropertyZip.objects.all().order_by('zip'),
               'types': PropertyType.objects.all().order_by('type'),
               'properties': Property.objects.all().order_by('street_name')
               }
    if request.user.is_authenticated:
        context['history'] = History.objects.filter(user=request.user).order_by('-datetime_stamp')[:4]

    if 'heh' in request.GET:
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
            'first_image': x.propertyimage_set.first().image.url,
            'image_tag': x.property_description
        } for x in Property.objects.filter()]
        return JsonResponse({'data': filtered_properties})

    return render(request, 'property/frontpage.html', context)


def get_property_by_id(request, id):
    if request.user.is_authenticated:
        current_user = request.user.id
        if request.method == 'POST':
            if 'favourite' in request.POST:
                try:
                    Favourite.objects.create(property_id=id, user_id=current_user)
                except IntegrityError:
                    pass
            if 'cart' in request.POST:
                try:
                    Cart.objects.create(property_id=id, user_id=current_user)
                except IntegrityError:
                    pass
            if 'buy_now' in request.POST:
                return redirect('contact_info')
        timestamp = timezone.now()
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

@login_required
@transaction.atomic
def payment_info(request):
    if request.method == 'POST':
        form = PaymentInfo(data=request.POST)
        if form.is_valid():
            request.session['pay_info'] = form.data
            return redirect('review_purchase')
    return render(request, 'property/payment_info.html', {
        'payment_form': PaymentInfo(),
    })

@login_required
@transaction.atomic
def review_purchase(request):
    total = 0
    user = request.user
    profile = Profile.objects.get(user=user.id)
    pay_info = request.session.get('pay_info')
    timestamp = timezone.now()
    properties = Property.objects.filter(cart__user=user.id)
    for pro in properties:
        total += pro.price
    if request.method == 'POST':
        try:
            for prop in properties:
                Order.objects.create(
                    buyer_ssn=profile.ssn,
                    sold_street_name=prop.street_name,
                    sold_street_number=prop.street_number,
                    realtor_licence_num=prop.realtor.get_licence(),
                    sold_zip=prop.zip.get_zip(),
                    sale_date=timestamp,
                    customer=user,
                    sold_property=prop
                )
                Property.objects.filter(pk=prop.id).update(is_active=False)
                Cart.objects.filter(property=prop.id, user=user.id).delete()
                History.objects.filter(property=prop.id).delete()
                return redirect('frontpage')
        except IntegrityError:
            pass
    return render(request, 'property/review_purchase.html',
                  {
                      "pay_info": pay_info,
                      "properties": properties,
                      "user": user,
                      "profile": profile,
                      "total": total,
                      "confirm_form": OrderForm
                  })


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
