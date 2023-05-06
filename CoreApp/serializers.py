from rest_framework import serializers
from CoreApp.models import *

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'