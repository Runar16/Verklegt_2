from django.shortcuts import render, get_object_or_404
from property.models import Property
from realtor.models import Realtor

def index(request):
    context = {'realtors': Realtor.objects.filter().select_related()}
    return render(request, 'realtor/realtor.html', context)


def get_realtor_by_id(request, id):
    return render(request, 'realtor/details.html', {
        'realtor': get_object_or_404(Realtor, pk=id),
        'properties': Property.objects.filter(realtor_id__exact=id)
    })
