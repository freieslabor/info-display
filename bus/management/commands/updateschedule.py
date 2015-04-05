from django.core.management.base import BaseCommand, CommandError
from bus.models import BusSchedule
from bus.fields import TRANSPORT_TYPES
from django.conf import settings

from lxml import etree
from datetime import datetime
from pytz import timezone
from dateutil.tz import tzlocal


class Command(BaseCommand):
    args = '<station_id station_id ...>'
    help = 'Updates bus schedule and cleans departed buses.'

    def handle(self, *args, **options):
        if len(args) == 0:
            raise CommandError('No station id\'s given.')

        # insert new buses
        for station_id in args:
            parser = etree.XMLParser(ns_clean=True)
            # xml parsing and xpath magic
            url = 'http://mobil.efa.de/mobile3/XSLT_DM_REQUEST'
            args = '?outputFormat=xml&mode=direct&name_dm=' \
                + '%s&limit=30&type_dm=stopID' % station_id

            tree = etree.parse(url + args, parser)
            departures = tree.xpath('/itdRequest/itdDepartureMonitor' +
                                    'Request/itdDepartureList/itdDeparture[*]')

            for departure in departures:
                # date and time
                date = departure.xpath('./itdDateTime/itdDate')[0].attrib
                # convert date attributes to int
                date = {k: int(v) for k, v in date.items()}
                time = departure.xpath("./itdDateTime/itdTime")[0].attrib
                # convert time attributes to int
                time = {k: int(v) for k, v in time.items() if v.isdigit()}
                # create datetime object and localize it
                date_time = datetime(date['year'], date['month'],
                                     date['day'], time['hour'], time['minute'])
                date_time = timezone(settings.TIME_ZONE).localize(date_time)

                # line, number and direction
                lineElement = departure.xpath('./itdServingLine')[0]
                number = lineElement.get('number')
                direction = lineElement.get('direction')

                transport = lineElement.xpath('./itdNoTrain')[0].get('name')
                # reverse mapping
                transport_to_id = {v: k for k, v in TRANSPORT_TYPES}
                transport_id = transport_to_id[transport]

                # create bus schedule object and save it
                schedule = BusSchedule(date=date_time, station_id=station_id,
                                       line=number, direction=direction,
                                       transport_type=transport_id)
                schedule.save()

            self.stdout.write('Successfully updated schedule for station %s.'
                              % station_id)

        # clear departed buses
        BusSchedule.objects.filter(date__lt=datetime.now(tzlocal())).delete()
