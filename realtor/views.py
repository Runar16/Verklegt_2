from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'realtor/realtor.html')

def get_realtor_by_id(request, id):
    return render(request, 'realtor/details.html', {
        'realtor': get_object_or_404(Realtor, pk=id)
    })
