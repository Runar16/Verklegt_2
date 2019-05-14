from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from property.models import Property
from user.forms.profile_form import ProfileForm, UserForm
from user.models import History
from user.models import Profile


def index(request):
    return render(request, 'user/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('edit_profile')
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
    return render(request, 'user/cart.html', {
        'properties': Property.objects.filter(cart__user=request.user.id)
    })


def profile(request):
    context = {'user_info': Profile.objects.filter(user=request.user.id)}
    return render(request, 'user/profile.html', context)

