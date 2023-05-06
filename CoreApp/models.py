from django.db import models

class Config(models.Model):

    BOOL_TRUE = 'T'
    BOOL_FALSE = 'F'

    BOOL_CHOICES = [
        (BOOL_TRUE, 'True'),
        (BOOL_FALSE, 'False')
    ]

    name = models.CharField(unique=True, max_length=255)

    domain = models.CharField(max_length=255)
    backup_domain = models.CharField(max_length=255, null=True, blank=True, )

    need_update = models.CharField(max_length=1, choices=BOOL_CHOICES, default=BOOL_FALSE)
    force_update = models.CharField(max_length=1, choices=BOOL_CHOICES, default=BOOL_FALSE)

    normal_update_link = models.CharField(max_length=255, null=True, blank=True, )
    deep_update_link = models.CharField(max_length=255, null=True, blank=True, )