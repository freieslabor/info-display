from django.core.management.base import BaseCommand
from event_schedule.models import Event, CalendarFeed
from django.conf import settings

from datetime import datetime
from pytz import timezone
from dateutil.tz import tzlocal

from icalendar import Calendar
import urllib.request


class Command(BaseCommand):
    help = 'Updates event schedule and cleans past events.'

    def handle(self, *args, **options):
        # insert new events
        for ical in CalendarFeed.objects.all():
            with urllib.request.urlopen(ical.url) as f:
                cal = Calendar.from_ical(f.read())
                for event in cal.walk('vevent'):
                    # create datetime object and localize it
                    date = event['DTSTART'].dt
                    date_time = date.astimezone(timezone(settings.TIME_ZONE))

                    # create public transport schedule object and save it
                    schedule = Event(
                        date=date_time,
                        title=event['SUMMARY']
                    )
                    schedule.save()

            self.stdout.write('Successfully updated %s.' % ical.url)

        # clear past events
        Event.objects.filter(date__lt=datetime.now(tzlocal())).delete()
