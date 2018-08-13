from django.shortcuts import render
from .models import Services
from .serializers import ServicesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ServiceAPIView(APIView):
    """Service api view"""

    def get(self, request):
        """Retrieve facility list"""
        services = Services.objects.filter(active=True)
        instance = ServicesSerializer(services,
            context={'request': request}, many=True)
        return Response(data=instance.data,
            status=status.HTTP_200_OK)