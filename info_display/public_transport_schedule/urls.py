from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^schedule.json$', 'public_transport_schedule.views.schedule_json',
        name='schedule_data'),
    url(r'^$', TemplateView.as_view(template_name='schedule.html'),
        name='schedule'),
]
