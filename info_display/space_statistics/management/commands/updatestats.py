from django.core.management.base import BaseCommand
from space_statistics.models import SpaceHour

from datetime import datetime, timedelta
from dateutil.parser import parse
import pytz
import urllib.request
import json


class Command(BaseCommand):
    help = 'Updates space statistics.'

    def handle(self, *args, **options):
        space_archive_json = 'http://freieslabor.org/api/room_archive'
        with urllib.request.urlopen(space_archive_json) as f:
            archive = json.loads(f.readall().decode('utf-8'))
            # archive dates are local German dates
            tz = pytz.timezone('Europe/Berlin')
            date = tz.localize(parse(archive[0]['timestamp']))
            for i in range(len(archive)):
                # compare archive date to next archive date or current date
                if i == len(archive)-1:
                    cmp_date = tz.localize(datetime.now())
                else:
                    cmp_date = tz.localize(parse(archive[i+1]['timestamp']))

                while date < cmp_date:
                    space_hour = SpaceHour(
                        status=archive[i]['open'],
                        date=date,
                        day_of_month=date.day,
                        month=date.month,
                        year=date.year,
                        day_of_week=date.weekday(),
                        hour=date.hour
                    )
                    space_hour.save()

                    date += timedelta(hours=1)

                    # print percentage because this job might take a while
                if i % 50 == 0:
                    done = i*100 // len(archive)
                    self.stdout.write('%d%% done' % done)

        self.stdout.write('Successfully updated space statistics.')
