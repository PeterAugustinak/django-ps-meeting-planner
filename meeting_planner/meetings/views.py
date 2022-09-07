from django.shortcuts import render, get_object_or_404

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
