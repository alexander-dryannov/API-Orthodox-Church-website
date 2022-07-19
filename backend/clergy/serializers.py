from rest_framework import serializers
from .models import Cleric


class ClericSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleric
        fields = '__all__'
