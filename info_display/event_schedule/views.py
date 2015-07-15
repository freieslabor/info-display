from django.shortcuts import HttpResponse
from event_schedule.models import Event

from datetime import datetime
from dateutil.tz import tzlocal
import json


def schedule_json(request):
    """Returns schedule as json."""
    schedule = Event.objects.filter(date__gte=datetime.now(tzlocal()))
    schedule_ordered = schedule.order_by('date')
    schedule_json = [event.as_dict() for event in schedule_ordered[:5]]
    return HttpResponse(json.dumps(schedule_json),
                        content_type='application/json')
