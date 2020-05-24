# from rest_framework import viewsets
#
# from ayg.entities.fresh_contact import FreshContact
# from ayg.serializers.fresh_contact import FreshContactSerializer, WritableFreshContactSerializer
#
#
# class FreshContactViewSet(viewsets.ModelViewSet):
#
#     queryset = FreshContact.objects.all()
#     serializer_class = FreshContactSerializer
#
#     def get_serializer_class(self):
#         if self.action in ['create', 'update']:
#             return WritableFreshContactSerializer
#         else:
#             return FreshContactSerializer