"""Url mappings for meetings app"""

from django.contrib import admin
from django.urls import path

from meetings.views import meeting_detail, rooms

urlpatterns = [
    path('<int:id>', meeting_detail, name="meeting_detail"),
    path('rooms', rooms, name="rooms"),
]
