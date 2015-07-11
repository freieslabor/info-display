from django.contrib import admin
from .models import Accident
from .forms import AccidentForm


class AccidentAdmin(admin.ModelAdmin):
    form = AccidentForm

    list_display = (
        'title',
        'reporter',
        'time',
    )

    list_filter = (
        'reporter',
        'time',
    )

    search_fields = (
        'title',
        'description',
    )

    def save_model(self, request, obj, form, change):
        if not Accident.objects.filter(pk=obj.pk).exists() or\
           not obj.reporter:
            obj.reporter = request.user

        obj.save()

admin.site.register(Accident, AccidentAdmin)
