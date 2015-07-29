from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^dow.json$', 'space_statistics.views.aggregate_dow',
        name='aggregate_dow'),
    url(r'^hour.json$', 'space_statistics.views.aggregate_hour',
        name='aggregate_hour'),
    url(r'^$', TemplateView.as_view(
        template_name='space_statistics/stats.html'), name='stats'),
]
