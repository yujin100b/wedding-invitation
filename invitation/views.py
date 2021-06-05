
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import LetterSerializer, AttendanceSerializer, CheeringSerializer, FundingSerializer, SubscriberSerializer
from .models import Letter, Attendance, Cheering, Funding, Subscriber


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class CheeringViewSet(viewsets.ModelViewSet):
    queryset = Cheering.objects.all()
    serializer_class = CheeringSerializer


class FundingViewSet(viewsets.ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
