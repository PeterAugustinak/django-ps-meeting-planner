"""Url mappings for meetings app"""

from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.meeting_detail, name="meeting_detail"),
    path('rooms', views.rooms, name="rooms"),
    path('new', views.new_meeting, name="new")
]
