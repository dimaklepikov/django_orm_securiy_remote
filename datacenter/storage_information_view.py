from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, format_duration
from django.shortcuts import render
import django


def storage_information_view(request):
    # Программируем здесь
    active_visits = Visit.objects.filter(leaved_at=None)
    not_closed_visits = []
    for visit in active_visits:
        name = visit.passcard.owner_name
        enter_time = django.utils.timezone.localtime(visit.entered_at)
        non_closed_visits = {
            "who_entered": name,
            "entered_at": enter_time,
            "duration": format_duration(get_duration(visit)),
        }
        not_closed_visits.append(non_closed_visits)
    context = {
        "non_closed_visits": not_closed_visits,
    }
    return render(request, 'storage_information.html', context)
