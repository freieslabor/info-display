from django.db import models
from django.contrib.auth.models import User


class Accident(models.Model):
    reporter = models.ForeignKey(
        User,
        related_name='+',
        verbose_name='Reporter',
        editable=False,
        null=True,
        blank=True
    )

    time = models.DateTimeField(
        verbose_name='Time'
    )

    casualties = models.IntegerField(
        verbose_name='Casualties',
        default=1
    )

    title = models.CharField(
        verbose_name='Title',
        max_length=55
    )

    description = models.TextField(
        verbose_name='Description',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['time']
