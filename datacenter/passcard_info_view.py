from datacenter.models import Passcard
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    context = {
        "passcard": passcard,
    }
    return render(request, 'passcard_info.html', context)
