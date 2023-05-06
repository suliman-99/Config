from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from CoreApp.serializers import *


class ConfigViewSet(GenericViewSet, RetrieveModelMixin):
    serializer_class = ConfigSerializer
    queryset = Config.objects.all()
    lookup_field = 'name'
    
