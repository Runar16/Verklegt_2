from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'realtor/realtor.html')

def realtors(request):
    return render(request, 'user/../templates/realtor/realtor.html')
