from rest_framework import serializers

from ayg.models import Youth
from ayg.serializers.youth_basic_detail import YouthBasicDetailSerializer


class YouthSerializer(YouthBasicDetailSerializer):

    groups = serializers.StringRelatedField(many=True)
    follows_vip = serializers.StringRelatedField(many=True)
    follows_youths = serializers.StringRelatedField(many=True)

    class Meta:
        model = Youth
        fields = YouthBasicDetailSerializer.Meta.fields + [
            'id',
            'referred_by',
            'groups',
            'status',
            'follow_up_status',
            'date_of_joining',
            'is_karyakarta',
            'followers',
            'follows_youths',
            'follows_vip'
        ]



class WritableYouthSerializer(YouthBasicDetailSerializer):

    class Meta:
        model = Youth
        fields = YouthBasicDetailSerializer.Meta.fields + [
            'id',
            'referred_by',
            'groups',
            'status',
            'follow_up_status',
            'date_of_joining',
            'is_karyakarta',
            'followers',
            'follows_youths',
            'follows_vip'
        ]