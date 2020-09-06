from django.db import models
import django


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )


def get_duration(visit):
    if visit.leaved_at is None:
        spent_time = django.utils.timezone.localtime() - visit.entered_at
        return spent_time
    else:
        return visit.leaved_at - visit.entered_at


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    spent_time_string = f'{hours}ч {minutes}мин'
    return spent_time_string


def is_visit_long(visit, minutes=60):
    duration_seconds = get_duration(visit).seconds
    duration_minutes = (duration_seconds % 3600) // 60
    if visit.leaved_at is None and duration_minutes > minutes:
        return True
    elif visit.leaved_at is None and duration_minutes < minutes:
        return False
    stay_seconds = (visit.leaved_at - visit.entered_at).seconds
    stay_minutes = (stay_seconds % 3600) // 60
    if visit.leaved_at is not None and stay_minutes > minutes:
        return True
    elif visit.leaved_at is not None and stay_minutes < minutes:
        return False
    else:
        return False
