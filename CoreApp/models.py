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
    
    current_version = models.PositiveIntegerField(default=0)
    last_accepted_version = models.PositiveIntegerField(default=0)

    normal_download_link = models.CharField(max_length=255, null=True, blank=True, )
    deep_download_link = models.CharField(max_length=255, null=True, blank=True, )


class Contact(models.Model):

    config = models.ForeignKey(Config, on_delete=models.CASCADE, related_name='contacts')

    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
