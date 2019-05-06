from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def realtors(request):
    return render(request, 'user/realtors.html')

