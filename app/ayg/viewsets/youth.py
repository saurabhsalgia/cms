from rest_framework import viewsets

from ayg.models import Youth
from ayg.serializers.youth import YouthSerializer, WritableYouthSerializer


class YouthViewSet(viewsets.ModelViewSet):

    queryset = Youth.objects.all()
    serializer_class = YouthSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return WritableYouthSerializer
        else:
            return YouthSerializer