from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.index_template = 'admin/home.html'

urlpatterns = patterns(
    '',
    url(r'^info-screen/$', 'info_screen.views.info_screen',
        name='info_screen'),
    url(r'', include(admin.site.urls)),
)
