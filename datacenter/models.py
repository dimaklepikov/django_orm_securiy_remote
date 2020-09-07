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
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)
    passcard = models.ForeignKey(Passcard)

    @property
    def duration(self):
        if not self.leaved_at:
            return django.utils.timezone.localtime() - self.entered_at
        else:
            return self.leaved_at - self.entered_at

    @property
    def duration_beautify(self):
        seconds = self.duration.total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        spent_time_string = f'{hours}ч {minutes}мин'
        return spent_time_string

    @property
    def is_long(self, minutes=60):
        overtime = 'Подозрительный' if self.duration.total_seconds() // 60 > minutes else 'Нормальный'
        return overtime

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
