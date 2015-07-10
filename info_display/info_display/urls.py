from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^info-screen/$', 'info_display.views.info_screen',
        name='info_screen'),
    url(r'^bus/', include('bus.urls', namespace='bus', app_name='bus')),
    url(r'', include(admin.site.urls)),
]
