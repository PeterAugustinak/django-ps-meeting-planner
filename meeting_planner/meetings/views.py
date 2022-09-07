from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Meeting, Room

# Create your views here.
def meeting_detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)

    return render(
        request,
        "meetings/detail.html",
        {"meeting": meeting},
    )

def rooms(request):
    num_of_rooms = Room.objects.count()
    rooms = Room.objects.all()

    return render(
        request,
        "meetings/rooms.html",
        {
            "num_of_rooms": num_of_rooms,
            "rooms": rooms,
        },
    )

MeetingForm = modelform_factory(Meeting, exclude=[])

def new_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()

    return render(
        request,
        "meetings/new.html",
        {"form": form},
    )
