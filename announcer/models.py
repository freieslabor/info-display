from django.db import models
from django.contrib.auth.models import User


class Announcement(models.Model):
    author = models.ForeignKey(
        User,
        related_name='+',
        verbose_name='Reporter'
    )

    title = models.CharField(
        verbose_name='Title',
        max_length=256
    )

    created = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True,
        editable=False
    )

    body = models.TextField(
        verbose_name='body'
    )
