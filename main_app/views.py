from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Boat
from .forms import CleaningForm

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
  cleaning_form = CleaningForm()
  return render(request, 'boats/detail.html', { 
    'boat': boat, 'cleaning_form': cleaning_form 
  })

def add_cleaning(request, boat_id):
  form = CleaningForm(request.POST)
  if form.is_valid():
    new_cleaning = form.save(commit=False)
    new_cleaning.boat_id = boat_id
    new_cleaning.save()
  return redirect('detail', boat_id=boat_id)

class BoatCreate(CreateView):
  model = Boat
  fields = '__all__'

class BoatUpdate(UpdateView):
  model = Boat
  fields = ['manufacturer', 'model', 'length', 'beam', 'year', 'description']

class BoatDelete(DeleteView):
  model = Boat
  success_url = '/boats/'