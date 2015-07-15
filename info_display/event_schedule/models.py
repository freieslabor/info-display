from django.db import models
from django.conf import settings

from pytz import timezone


class Event(models.Model):
    date = models.DateTimeField('date of departure')
    title = models.CharField(max_length=20)

    def __str__(self):
        return '%s am %s' % (self.title, self.date)

    def as_dict(self):
        date_tz = self.date.astimezone(timezone(settings.TIME_ZONE))
        return dict(
            date=date_tz.isoformat(),
            title=self.title,
        )


class CalendarFeed(models.Model):
    url = models.CharField(
        verbose_name='ical feed',
        max_length=256
    )

    def __str__(self):
        return self.url
