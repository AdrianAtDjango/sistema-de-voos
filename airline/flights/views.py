from django.shortcuts import render
from .models import Flight

def index(request):
    flights = Flight.objects.all()
    context = {
        "flights": flights
    }
    return render(request, "index.html", context)