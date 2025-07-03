from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *

def index(request):
    flights = Flight.objects.all()
    context = {
        "flights": flights
    }
    return render(request, "index.html", context)

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passenger = flight.passenger.all()
    context = {"flight": flight, "passengers": passenger}
    return render(request, "flight.html", context)

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(id=flight_id)
        passenger = Passenger.objects.get(id=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return redirect(reverse("flight", args=(flight.id,)))