from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^info-screen/$', 'info_screen.views.info_screen',
        name='info_screen'),
    url(r'^bus/', include('bus.urls', namespace='bus', app_name='bus')),
    url(r'^event-schedule/', include('event_schedule.urls', namespace='event_schedule', app_name='event_schedule')),
    url(r'', include(admin.site.urls)),
]
