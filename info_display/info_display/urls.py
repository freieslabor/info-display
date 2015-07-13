from django.conf.urls import include, url
from django.contrib import admin

screen_urlpatterns = [
    url(r'^public_transport_schedule/(?P<id>\w+)/',
        include('public_transport_schedule.urls',
                namespace='public_transport_schedule',
                app_name='public_transport_schedule')),
    url(r'^days_without_an_accident/',
        include('days_without_an_accident.urls',
                namespace='days_without_an_accident',
                app_name='days_without_an_accident')),
]

urlpatterns = [
    url(r'^screens/', include(screen_urlpatterns)),
    url(r'^main-screen/$', 'info_display.views.main_screen',
        name='main_screen'),
    url(r'', include(admin.site.urls)),
]
