from rest_framework import serializers

from ayg.models import YouthBasicDetail


class YouthBasicDetailSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=30, trim_whitespace=True)
    middle_name = serializers.CharField(max_length=30, trim_whitespace=True, allow_blank=True)
    last_name = serializers.CharField(max_length=30, trim_whitespace=True)
    phone_number = serializers.CharField(max_length=20, trim_whitespace=True, allow_blank=True)

    class Meta:
        model = YouthBasicDetail
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'address',
            'date_of_birth',
            'occupation'
        ]
