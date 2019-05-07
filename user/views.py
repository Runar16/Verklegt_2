from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def realtors(request):
    return render(request, 'user/realtors.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })