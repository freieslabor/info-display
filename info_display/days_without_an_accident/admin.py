# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Accident
from forms import AccidentForm


class AccidentAdmin(admin.ModelAdmin):
    form = AccidentForm

    list_display = (u'id', 'reporter', 'description', 'created')
    list_filter = ('reporter', 'created')


admin.site.register(Accident, AccidentAdmin)
