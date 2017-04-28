from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

screen_urlpatterns = [
    url(r'^public_transport_schedule/(?P<id>\w+)/',
        include('info_display.screens.public_transport_schedule.urls',
                namespace='public_transport_schedule',
                app_name='public_transport_schedule')),
    url(r'^days_without_an_accident/',
        include('info_display.screens.days_without_an_accident.urls',
                namespace='days_without_an_accident',
                app_name='days_without_an_accident')),
    url(r'^event_schedule/',
        include('info_display.screens.event_schedule.urls',
                namespace='event_schedule',
                app_name='event_schedule')),

]

urlpatterns = [
    url(r'^screens/', include(screen_urlpatterns)),
    url(r'^main-screen/$', 'info_display.views.main_screen',
        name='main_screen'),
    url(r'', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns = staticfiles_urlpatterns() + urlpatterns
