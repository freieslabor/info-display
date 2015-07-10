from django import template
from django.conf import settings as django_settings

register = template.Library()


@register.filter
def settings(attr):
    return getattr(django_settings, attr, None)
