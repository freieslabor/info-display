from django.db import models
from django.contrib.auth.models import User


class Accident(models.Model):
    reporter = models.ForeignKey(
        User,
        related_name='+',
        verbose_name='Reporter'
    )

    description = models.TextField(
        verbose_name='Description',
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        verbose_name='Created'
    )
