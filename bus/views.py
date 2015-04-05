from django.shortcuts import render, HttpResponse
from django.core import serializers
from bus.models import BusSchedule

from datetime import datetime
from dateutil.tz import tzlocal
import json


def schedule_json(request):
    """Returns schedule as json."""
    schedule = BusSchedule.objects.filter(date__gte=datetime.now(tzlocal()))
    schedule_json = [bus.as_json() for bus in schedule[:5]]
    return HttpResponse(json.dumps(schedule_json),
                        content_type='application/json')
