from dateutil.tz import tzlocal
from datetime import datetime
import json

from django.shortcuts import HttpResponse

from .models import PTSchedule


def schedule_json(request, id):
    """Returns schedule as json."""
    schedule = PTSchedule.objects.filter(date__gte=datetime.now(tzlocal()),
                                         station__dm_id=id)
    schedule_json = [connection.as_dict() for connection in schedule[:5]]
    return HttpResponse(json.dumps(schedule_json),
                        content_type='application/json')
