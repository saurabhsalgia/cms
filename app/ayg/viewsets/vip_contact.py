from rest_framework import viewsets

from ayg.models import VIPContact
from ayg.serializers.vip_contact import VIPContactSerializer, WritableVIPContactSerializer


class VIPContactViewSet(viewsets.ModelViewSet):

    queryset = VIPContact.objects.all()
    serializer_class = VIPContactSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return WritableVIPContactSerializer
        else:
            return VIPContactSerializer
