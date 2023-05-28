# rządania i odpowiedzi

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect



def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
