from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.forms.profile_form import ProfileForm, UserForm
from user.models import History


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
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'user/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def update_history(request):
    if request.method == 'POST':
        history = History.objects.get()
        history.user_id = request.POST['user_id']
        history.property_id = request.POST['property_id']
        history.save()
        message = 'Insert successful'
    return HttpResponse(message)
