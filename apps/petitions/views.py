from django.shortcuts import render
from .models import Services
from .serializers import ServicesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
# Create your views here.

class ServiceAPIView(APIView):
    """Service api view"""

    def get(self, request,name):
        """Get Services list"""

        data = self.get_type_data(name,'get')
        return Response(data=data['data'],
            status=data['status'])


    def post(self, request,name,format=None):
        
        data = self.get_type_data(name,'post')        
        return Response(data=data['data'],
            status=data['status'])

    def put(self, request, name, format=None):
        
        data = self.get_type_data(name,'put')
        return Response(data=data['data'],
            status=data['status'])
   
    def delete(self, request, name, format=None):

        data = self.get_type_data(name,'delete')
        return Response(data=data['data'],
            status=data['status'])
    

    def get_type_data(self, name,option):

        try:
            service = Services.objects.get(active=True,name=name)
        except Services.DoesNotExist:
            service = None

        print(service)

        if service is None:
            obj ={"data": "Not found"}
            return {'data': obj, 'status': 404}

        if service.type == option:
            print(type(service.requests))
            requestJson = {}
            requestJson['data'] = json.loads(service.response)
            requestJson['status'] = service.status
            return requestJson
        else:
            obj ={"data": "Error server"}
            return {'data': obj, 'status': 500}
