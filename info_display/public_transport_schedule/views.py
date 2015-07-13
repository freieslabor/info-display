from django.shortcuts import HttpResponse
from public_transport_schedule.models import PTSchedule

from datetime import datetime
from dateutil.tz import tzlocal
import json


def schedule_json(request, id):
    """Returns schedule as json."""
    schedule = PTSchedule.objects.filter(date__gte=datetime.now(tzlocal()),
                                         station__dm_id=id)
    schedule_json = [connection.as_dict() for connection in schedule[:5]]
    return HttpResponse(json.dumps(schedule_json),
                        content_type='application/json')
