from django.conf.urls import include, url
from django.contrib import admin

screen_urlpatterns = [
    url(r'^bus/', include('bus.urls', namespace='bus', app_name='bus')),
]

urlpatterns = [
    url(r'^screens/', include(screen_urlpatterns)),
    url(r'^main-screen/$', 'info_display.views.main_screen',
        name='main_screen'),
    url(r'', include(admin.site.urls)),
]
