from django.shortcuts import HttpResponse
from django.db.models import Count
from space_statistics.models import SpaceHour

import json
import pytz
from datetime import datetime


def aggregate_dow(request):
    """Returns space stats aggregated by day of week as json."""
    return aggregated_status('day_of_week')


def aggregate_hour(request):
    """Returns space stats aggregated by hour as json."""
    return aggregated_status('hour')


def aggregated_status(attribute):
    """Returns space stats aggregated by given attribute name."""
    aggregated = SpaceHour.objects.values(attribute) \
        .annotate(Count('status')).filter(status=True)

    hours_total = SpaceHour.objects.count() / 7
    aggregated = [
        {
            attribute: status[attribute],
            'count': status['status__count'],
            'percentage': (status['status__count'] / hours_total)*100
        }
        for status in list(aggregated)
    ]
    return HttpResponse(json.dumps(aggregated),
                        content_type='application/json')
