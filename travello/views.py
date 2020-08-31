from django.shortcuts import render
from . models import Destination
# Create your views here.

def index(request):
    
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.price = 700
    dest1.image = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'Biryani'
    dest2.price = 680
    dest2.image = 'destination_2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Banglore'
    dest3.desc = 'IT hub'
    dest3.price = 500
    dest3.image = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]
    
    return render(request,"index.html", {'dests': dests})