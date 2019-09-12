from django.forms import ModelForm
from django import forms
from .models import Cleaning
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CleaningForm(ModelForm):
  class Meta:
    model = Cleaning
    fields = ['date', 'cleaning']

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']