from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner app!")


def date(request):
    date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    return HttpResponse(f'This page was server at {date}')


def about(request):
    about_me = 'I am at start of Django journey'
    return HttpResponse(f'About me: {about_me}.')
