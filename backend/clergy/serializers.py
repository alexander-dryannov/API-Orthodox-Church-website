from .models import Cleric
from rest_framework import serializers


class ClericSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleric
        fields = '__all__'
