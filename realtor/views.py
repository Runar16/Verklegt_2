from django.shortcuts import render, get_object_or_404
from realtor.models import Realtor
from property.views import get_property_by_realtor_id

def index(request):
    context = {'realtors': Realtor.objects.filter().select_related()}
    return render(request, 'realtor/realtor.html', context)


def get_realtor_by_id(request, id):
    return render(request, 'realtor/details.html', {
        'realtor': get_object_or_404(Realtor, pk=id),
        'properties': get_property_by_realtor_id(request, id)
    })
