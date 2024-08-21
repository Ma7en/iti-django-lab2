from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def track_list(request):
    tracks = [
        {"id": 1, "name": "python", "description": "track python"},
        {"id": 2, "name": "java", "description": "track java"},
        {"id": 3, "name": "c++", "description": "track c++"},
    ]
    context = {}
    context["tracks"] = tracks
    return render(request, "track/list.html", context)
    # return HttpResponse("<h1>track List</h1>")


def track_create(request):
    # return HttpResponse("<h1>track create</h1>")
    return render(request, "track/create.html")


def track_update(request, id):
    # return HttpResponse("<h1>track update</h1>")
    context = {}
    context = {"id": id}
    return render(request, "track/update.html", context)


def track_delete(request, id):
    # return HttpResponse("<h1>track delete</h1>")
    context = {}
    context = {"id": id}
    return render(request, "track/delete.html", context)


def track_details(request, id):
    # return HttpResponse(f"<h1>track Details: {id}</h1>")
    context = {}
    context = {"id": id}
    return render(request, "track/details.html", context)
