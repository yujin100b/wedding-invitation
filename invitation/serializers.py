from rest_framework import serializers
from .models import Letter, Attendance, Cheering, Funding, Subscriber


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class CheeringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheering
        fields = '__all__'


class FundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'