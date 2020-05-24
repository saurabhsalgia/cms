from rest_framework.routers import SimpleRouter

# from ayg.viewsets.fresh_contact import FreshContactViewSet
from ayg.viewsets.group import GroupViewSet
from ayg.viewsets.user import UserViewSet
from ayg.viewsets.vip_contact import VIPContactViewSet
from ayg.viewsets.youth import YouthViewSet

router = SimpleRouter()


router.register(r'v1/users', UserViewSet)
router.register(r'v1/youths', YouthViewSet)
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/vip-contacts', VIPContactViewSet)
# router.register(r'v1/fresh-contacts', FreshContactViewSet)

urlpatterns = router.urls