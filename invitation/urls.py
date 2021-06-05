from rest_framework import routers
from .views import LetterViewSet, AttendanceViewSet, CheeringViewSet, FundingViewSet, SubscriberViewSet

router = routers.SimpleRouter()
router.register(r'letter', LetterViewSet)
router.register(r'attend', AttendanceViewSet)
router.register(r'cheer', CheeringViewSet)
router.register(r'funding', FundingViewSet)
router.register(r'subscriber', SubscriberViewSet)
urlpatterns = router.urls
