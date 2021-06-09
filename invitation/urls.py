from rest_framework import routers
from django.urls import path
from . import views


router = routers.SimpleRouter()
router.register(r'attend', views.AttendanceViewSet)
router.register(r'cheer', views.CheeringViewSet)
router.register(r'funding', views.FundingViewSet)
router.register(r'subscriber', views.SubscriberViewSet)

urlpatterns = [
    path('hit/', views.hit),
    path('left_seat/', views.left_seat),
    path('funfact/', views.funfact),
]

urlpatterns += router.urls
