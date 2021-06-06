from rest_framework import routers
from django.urls import path
from . import views


router = routers.SimpleRouter()
router.register(r'letter', views.LetterViewSet)
router.register(r'attend', views.AttendanceViewSet)
router.register(r'cheer', views.CheeringViewSet)
router.register(r'funding', views.FundingViewSet)
router.register(r'subscriber', views.SubscriberViewSet)

urlpatterns = [
    path('hit/', views.hit),
    path('funfact/', views.funfact),
]

urlpatterns += router.urls
