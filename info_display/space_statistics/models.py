from django.db import models


class SpaceHour(models.Model):
    status = models.BooleanField('Status')
    date = models.DateTimeField('Date')
    day_of_month = models.IntegerField('Day of Month')
    month = models.IntegerField('Month')
    year = models.IntegerField('Year')
    day_of_week = models.IntegerField('Day of Week')
    hour = models.IntegerField('Hour')

    def __str__(self):
        door = 'open' if self.status else 'closed'
        return '%s: %s' % (self.date.strftime('%d.%m.%Y %H:00'), door)
