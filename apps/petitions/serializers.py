from .models import Services
from rest_framework import serializers


class ServicesSerializer(serializers.ModelSerializer):
    """ Services Serializer """

    class Meta:
        model = serializers
        fields = '__all__'