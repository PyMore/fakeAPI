from django.contrib import admin
from django.urls import path , include 
from .views import ServiceAPIView

urlpatterns = [
    path('fake/<slug:name>', ServiceAPIView.as_view()),
]
