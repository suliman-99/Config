from django.contrib import admin
from CoreApp.models import *


class ContactInline(admin.TabularInline):
    model = Contact
    classes = ['collapse']
    extra = 0


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    list_display = [
                    'id', 
                    'name', 
                    'domain',
                    'backup_domain',
                    'current_version',
                    'last_accepted_version',
                    'normal_download_link',
                    'deep_download_link',
                    ]