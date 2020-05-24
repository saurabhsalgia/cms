from rest_framework import serializers

from ayg.models import VIPContact


class VIPContactSerializer(serializers.ModelSerializer):

    followers = serializers.StringRelatedField(many=True)
    referred_by = serializers.StringRelatedField()

    class Meta:
        model = VIPContact
        fields = [
            'id',
            'name',
            'phone_number',
            'home_address',
            'office_address',
            'referred_by',
            'followers',
            'follow_up_status',
            'is_successful',
            'comments'
        ]


class WritableVIPContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = VIPContact
        fields = [
            'id',
            'name',
            'phone_number',
            'home_address',
            'office_address',
            'referred_by',
            'followers',
            'follow_up_status',
            'is_successful',
            'comments'
        ]