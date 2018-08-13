from django.contrib import admin
from django.urls import path , include 
from .views import ServiceAPIView

urlpatterns = [
    path('data/', ServiceAPIView.as_view()),
]
