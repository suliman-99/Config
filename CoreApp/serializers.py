from rest_framework import serializers
from CoreApp.models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['key', 'value']

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ['name', 'domain', 'backup_domain', 'need_update', 'force_update',
                  'normal_download_link', 'deep_download_link', 'contacts']


    contacts = ContactSerializer(many=True)

    need_update = serializers.SerializerMethodField()
    force_update = serializers.SerializerMethodField()

    def get_need_update(self, instance: Config):
        request_version = int(self.context['request'].query_params.get('version'))
        return 'T' if request_version < instance.current_version else 'F'

    def get_force_update(self, instance: Config):
        request_version = int(self.context['request'].query_params.get('version'))
        return 'T' if request_version < instance.last_accepted_version else 'F'
    
        