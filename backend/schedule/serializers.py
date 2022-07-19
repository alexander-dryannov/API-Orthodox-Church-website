from dataclasses import fields
from rest_framework import serializers
from .models import Schedule


# Все поля
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
