from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from meetings.models import Meeting


def welcome(request):
    num_of_meetings = Meeting.objects.count()
    lst_of_meetings = Meeting.objects.all()

    return render(
        request,
        'website/welcome.html',
        {
            "num_of_meetings": num_of_meetings,
            "meetings": lst_of_meetings,
         }
    )


def date(request):
    date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    return HttpResponse(f'This page was server at {date}')


def about(request):
    about_me = 'I am at start of Django journey'
    return HttpResponse(f'About me: {about_me}.')
