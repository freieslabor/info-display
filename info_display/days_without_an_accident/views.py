from django.http import JsonResponse
from django.utils import timezone
from .models import Accident


def last_accident(request):
    last_accident = Accident.objects.last()

    if not last_accident:
        return JsonResponse({
            'last_accident': last_accident,
        })

    return JsonResponse({
        'last_accident': {
            'title': last_accident.title,
            'description': last_accident.description,
            'time': last_accident.time,
            'casualties': last_accident.casualties,
        },
        'days': (timezone.now() - last_accident.time).days,
    })
