from rest_framework import viewsets
from rest_framework.decorators import action

from ayg.models import Group, Youth
from ayg.serializers.group import GroupSerializer, WritableGroupSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return WritableGroupSerializer
        else:
            return GroupSerializer
