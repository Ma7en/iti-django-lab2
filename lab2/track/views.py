from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def track_list(request):
    context = {}
    tracks = Track.objects.all()
    context["tracks"] = tracks
    return render(request, "track/list.html", context)


def track_create(request):
    return render(request, "track/create.html")


def track_update(request, id):
    context = {}
    context = {"id": id}
    return render(request, "track/update.html", context)


def track_delete(request, id):
    context = {}
    try:
        trackobj = Track.objects.get(id=id)  # Fetch the trainee to be deleted
        if request.method == "GET":
            trackobj.delete()
            return redirect("trainee_list")
        context["trainee"] = trackobj
    except Track.DoesNotExist:
        return HttpResponse("Trainee not found", status=404)

    return render(request, "track/delete.html", context)


def track_details(request, id):
    context = {}
    trackobj = Track.objects.get(id=id)  # Fetch record from the database
    context["track"] = trackobj
    return render(request, "track/details.html", context)
