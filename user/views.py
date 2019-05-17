from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from property.models import Property
from realtor.models import Realtor
from user.forms.profile_form import ProfileForm, UserForm
from user.forms.register_form import RegisterProfileForm
from user.models import History, Cart, Favourite, Profile


def index(request):
    return render(request, 'user/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterProfileForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.zip = form.cleaned_data.get('zip')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.street_name = form.cleaned_data.get('street_name')
            user.profile.street_number = form.cleaned_data.get('street_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = RegisterProfileForm()
    return render(request, 'user/register.html', {
        'form': form,
    })


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        print("i am the law")
        print(request.FILES)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            print(profile_form.cleaned_data)

            user_form.save()
            goat = profile_form.save()
            print(goat.profile_picture)
            #messages.success(request, 'Your profile was successfully updated!')

        else:
            messages.error(request, 'Please correct the error below.')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'user/change_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@csrf_protect
def update_history(request):
    if request.method == 'POST':
        history = History.objects.get()
        history.user_id = request.POST['user_id']
        history.property_id = request.POST['property_id']
        history.save()
        message = 'Insert successful'
    return HttpResponse(message)


def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        password_form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'password_form': password_form
    })


def cart(request):
    total = 0
    user_id = request.user.id
    properties = Property.objects.filter(cart__user=request.user.id)
    for pro in properties:
        total += pro.price
    if request.method == 'POST':
        prop = request.POST['property_id']
        try:
            Cart.objects.filter(property=prop, user=user_id).delete()
        except IntegrityError:
            pass
        return redirect('cart')
    return render(request, 'user/cart.html', {
        'properties': Property.objects.filter(cart__user=request.user.id),
        'total': total
    })


def favourite(request):
    total = 0
    user_id = request.user.id
    properties = Property.objects.filter(favourite__user=request.user.id)
    for pro in properties:
        total += pro.price
    if request.method == 'POST':
        prop = request.POST['property_id']
        if 'add_to_cart' in request.POST:
            try:
                Cart.objects.create(property_id=prop, user_id=user_id)
            except IntegrityError:
                pass
        if 'delete_property' in request.POST:
            try:
                Favourite.objects.filter(property=prop, user=user_id).delete()
            except IntegrityError:
                pass
    return render(request, 'user/favourite.html', {
        'properties': Property.objects.filter(favourite__user=request.user.id),
        'total': total
    })


def profile(request):
    if request.method == 'POST':
        user = request.user
        try:
            User.objects.filter(pk=user.id).delete()
            Cart.objects.filter(user=user.id).delete()
            History.objects.filter(user=user.id).delete()
            Profile.objects.filter(user=user.id).delete()
            if user.is_staff:
                Realtor.objects.filter(user=user.id).delete()
        except IntegrityError:
            pass
    context = {'user_info': request.user.profile,
               'history': History.objects.filter(user=request.user).order_by('-datetime_stamp')}
    return render(request, 'user/profile.html', context)


def upload_image(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        image = request.FILES
        profile_form = ProfileForm(request.POST, image or None, instance=request.user.profile)
        if profile_form.is_valid() and user_form.is_valid():
            if image is not None:
                new_profile = profile_form.save()
                return new_profile
            else:
                return None

        else:
            return edit_profile(profile_form)