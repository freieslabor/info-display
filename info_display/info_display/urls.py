from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^main-screen/$', 'info_display.views.main_screen',
        name='main_screen'),
    url(r'^bus/', include('bus.urls', namespace='bus', app_name='bus')),
    url(r'', include(admin.site.urls)),
]
