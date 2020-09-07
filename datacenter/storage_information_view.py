from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import django


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    context = {
        "visits": visits,
    }
    return render(request, 'storage_information.html', context)
