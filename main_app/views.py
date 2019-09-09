from django.shortcuts import render
from .models import Boat

# Create Views Here

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def boats_index(request):
  boats = Boat.objects.all()
  return render(request, 'boats/index.html', { 'boats': boats })

def boat_detail(request, boat_id):
  boat = Boat.objects.get(id=boat_id)
  return render(request, 'boats/detail.html', { 'boat': boat })