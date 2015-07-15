from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^schedule.json$', 'event_schedule.views.schedule_json',
        name='event_data'),
    url(r'^$', TemplateView.as_view(template_name='event_schedule/schedule.html'),
        name='event_schedule'),
]
