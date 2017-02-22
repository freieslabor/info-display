from pytz import timezone

from django.db import models
from django.conf import settings

from .fields import TRANSPORT_TYPES


class PTSchedule(models.Model):
    date = models.DateTimeField('date of departure')
    station = models.ForeignKey('Station')
    line = models.CharField(max_length=20)
    direction = models.CharField(max_length=50)
    transport_type = models.IntegerField(choices=TRANSPORT_TYPES)

    id_to_transport = dict(TRANSPORT_TYPES)

    class Meta:
        unique_together = (("date", "station", "line", "direction",
                            "transport_type"),)

    def __str__(self):
        return 'date: %s, station: %d, line: %s, direction: %s, type: %s' \
            % (self.date, self.station_id, self.line, self.direction,
                self.id_to_transport[self.transport_type])

    def as_dict(self):
        date_tz = self.date.astimezone(timezone(settings.TIME_ZONE))
        return dict(
            date=date_tz.isoformat(),
            station_name=self.station.name,
            line=self.line,
            direction=self.direction,
            transport_type=self.id_to_transport[self.transport_type],
        )


class Station(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=30
    )

    dm_id = models.IntegerField(
        verbose_name='ID',
    )

    def __str__(self):
        return self.name
