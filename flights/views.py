from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport, flight, Passenger

# Create your views here.
def index(request):
    all_flights = flight.objects.all()
    # print(all_flights)
    return render(request, 'flights/index.html', {'flights': all_flights})

def flight_(request, flight_id):
    my_flight = flight.objects.all().filter(id__exact=flight_id)[0]
    my_passengers = Passenger.objects.all().filter(flights=my_flight)
    return render(request, 'flights/flight.html', {'flight': my_flight, 'passengers': my_passengers})