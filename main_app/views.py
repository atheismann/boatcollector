from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Boat, Sail, Photo
from .forms import CleaningForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'boatcollector-ajt'

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
  sails_boat_doesnt_have = Sail.objects.exclude(id__in = boat.sails.all().values_list('id'))
  cleaning_form = CleaningForm()
  return render(request, 'boats/detail.html', { 
    'boat': boat, 'cleaning_form': cleaning_form, 
    'sails': sails_boat_doesnt_have
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

class SailList(ListView):
  model = Sail

class SailDetail(DetailView):
  model = Sail

class SailCreate(CreateView):
  model = Sail
  fields = '__all__'

class SailUpdate(UpdateView):
  model = Sail
  fields = ['name', 'type']

class SailDelete(DeleteView):
  model = Sail
  success_url = '/sails/'

def assoc_sail(request, boat_id, sail_id):
  Boat.objects.get(id=boat_id).sails.add(sail_id)
  return redirect('detail', boat_id=boat_id)

def unassoc_sail(request, boat_id, sail_id):
  Boat.objects.get(id=boat_id).sails.remove(sail_id)
  return redirect('detail', boat_id=boat_id)

def add_photo(request, boat_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
      s3 = boto3.client('s3')
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      try:
          s3.upload_fileobj(photo_file, BUCKET, key)
          url = f"{S3_BASE_URL}{BUCKET}/{key}"
          photo = Photo(url=url, boat_id=boat_id)
          photo.save()
      except:
          print('An error occurred uploading file to S3')
  return redirect('detail', boat_id=boat_id)