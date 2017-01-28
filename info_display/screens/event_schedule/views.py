from dateutil.tz import tzlocal
from datetime import datetime
import json

from django.shortcuts import HttpResponse

from .models import Event


def schedule_json(request):
    """Returns schedule as json."""
    schedule = Event.objects.filter(date__gte=datetime.now(tzlocal()))
    schedule_ordered = schedule.order_by('date')
    schedule_json = [event.as_dict() for event in schedule_ordered[:5]]
    return HttpResponse(json.dumps(schedule_json),
                        content_type='application/json')
