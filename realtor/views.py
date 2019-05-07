from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'realtors': Realtor.objects.all().order_by('user.first_name')}
    return render(request, 'realtor/realtor.html',context)


def get_realtor_by_id(request, id):
    return render(request, 'realtor/details.html', {
        'realtor': get_object_or_404(Realtor, pk=id)
    })
