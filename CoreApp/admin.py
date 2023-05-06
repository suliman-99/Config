from django.contrib import admin
from CoreApp.models import *


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = [
                    'id', 
                    'name', 
                    'domain',
                    'backup_domain',
                    'force_update',
                    'need_update',
                    'normal_update_link',
                    'deep_update_link',
                    ]