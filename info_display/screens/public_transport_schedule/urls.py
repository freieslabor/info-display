from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^schedule.json$', 'info_display.screens.public_transport_schedule.views.schedule_json',
        name='schedule_data'),
    url(r'^$', TemplateView.as_view(template_name='public_transport_schedule/schedule.html'),
        name='schedule'),
]
