from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    'info_display.screens.days_without_an_accident.views',
    url(r'^last_accident.json$', 'last_accident', name='last_accident'),
    url(r'', TemplateView.as_view(
        template_name='days_without_an_accident/sign.html'), name='sign'),
)
