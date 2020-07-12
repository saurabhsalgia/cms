from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ayg.models import Youth, YouthBasicDetail
from ayg.serializers.youth import YouthSerializer, WritableYouthSerializer


class YouthViewSet(viewsets.ModelViewSet):

    queryset = Youth.objects.all()
    serializer_class = YouthSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return WritableYouthSerializer
        else:
            return YouthSerializer

    @action(url_path='choices', detail=False)
    def get_choices(self, request):
        choice = request.query_params.get('choice')
        choice_options = {
            'occupations': YouthBasicDetail.OCCUPATION_CHOICES,
            'follow_up_status': Youth.FOLLOW_UP_STATUS_CHOICES,
            'weekly_forum_status': Youth.WEEKLY_FORUM_STATUS_CHOICES
        }
        correct_options = [choice for choice in choice_options]
        if choice in correct_options:
            choices = choice_options.get(choice)
            return Response([{'code':code, 'value': choice} for code, choice in choices])
        return Response({
            'error': f'Please provide a valid choice. Options are {correct_options}'
        }, status=status.HTTP_400_BAD_REQUEST)
