# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Announcement
from forms import AnnouncementForm


class AnnouncementAdmin(admin.ModelAdmin):
    form = AnnouncementForm

    list_display = ('title', 'author', 'created')
    list_filter = ('author', 'created')


admin.site.register(Announcement, AnnouncementAdmin)
