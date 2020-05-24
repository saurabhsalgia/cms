# class FreshContactSerializer(YouthBasicDetailSerializer):
#
#     referred_by = UserSerializer()
#     fresh_youth_follower = UserSerializer(many=True)
#     groups = GroupSerializer(many=True)
#
#     class Meta:
#         model = FreshContact
#         fields = YouthBasicDetailSerializer.Meta.fields + [
#             'id',
#             'referred_by',
#             'weekly_forum_joined',
#             'follow_up_status',
#             'groups',
#             'fresh_youth_follower'
#         ]
#
#
# class WritableFreshContactSerializer(YouthBasicDetailSerializer):
#
#     class Meta:
#         model = FreshContact
#         fields = YouthBasicDetailSerializer.Meta.fields + [
#             'id',
#             'referred_by',
#             'weekly_forum_joined',
#             'follow_up_status',
#             'groups',
#             'fresh_youth_follower'
#         ]