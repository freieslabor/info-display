from django.db import models
from public_transport_schedule.fields import TRANSPORT_TYPES
from django.conf import settings

from pytz import timezone


class PTSchedule(models.Model):
    date = models.DateTimeField('date of departure')
    station_id = models.IntegerField()
    line = models.CharField(max_length=20)
    direction = models.CharField(max_length=50)
    transport_type = models.IntegerField(choices=TRANSPORT_TYPES)

    id_to_transport = dict(TRANSPORT_TYPES)

    def __str__(self):
        return 'date: %s, station: %d, line: %s, direction: %s, type: %s' \
            % (self.date, self.station_id, self.line, self.direction,
                self.id_to_transport[self.transport_type])

    def as_json(self):
        date_tz = self.date.astimezone(timezone(settings.TIME_ZONE))
        return dict(
            date=date_tz.isoformat(),
            station_id=self.station_id,
            line=self.line,
            direction=self.direction,
            transport_type=self.id_to_transport[self.transport_type],
        )
