from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = patterns(
    '',
    url(r'^info-screen/$', 'info_screen.views.info_screen',
        name='info_screen'),
    url(r'^bus/schedule.json', 'bus.views.schedule_json'),
    url(r'^bus/', TemplateView.as_view(template_name='bus.html')),
    url(r'', include(admin.site.urls)),
)
