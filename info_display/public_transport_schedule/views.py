from django.shortcuts import render, HttpResponse
from django.core import serializers
from public_transport_schedule.models import PTSchedule

from datetime import datetime
from dateutil.tz import tzlocal
import json


def schedule_json(request):
    """Returns schedule as json."""
    schedule = PTSchedule.objects.filter(date__gte=datetime.now(tzlocal()))
    schedule_json = [connection.as_json() for connection in schedule[:5]]
    return HttpResponse(json.dumps(schedule_json),
                        content_type='application/json')
