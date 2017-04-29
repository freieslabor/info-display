from django.db import models
from django.conf import settings

class PartkeeprInstance(models.Model):
    api_url = models.CharField(
        verbose_name='partkeepr API URL',
        max_length=256
    )
    user = models.CharField(
        verbose_name='partkeepr user',
        max_length=256
    )
    password = models.CharField(
        verbose_name='partkeepr password',
        max_length=256
    )

    def __str__(self):
        return '%s (%s:%s)' % (self.api_url, self.user, self.password)
