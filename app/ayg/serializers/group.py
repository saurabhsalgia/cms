from rest_framework import serializers

from ayg.models import Group, Youth


class GroupSerializer(serializers.ModelSerializer):

    youths = serializers.StringRelatedField(many=True)
    owner = serializers.StringRelatedField()
    parent_group = serializers.StringRelatedField()
    child_groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'parent_group',
            'owner',
            'total_youths',
            'youths',
            'child_groups'
        ]

class WritableGroupSerializer(serializers.ModelSerializer):

    youths = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Youth.objects.all(), required=False)

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'parent_group',
            'owner',
            'youths'
        ]
