from django.contrib import admin
from .models import Boat, Cleaning, Sail, Photo

# Register your models here.

admin.site.register(Boat)
admin.site.register(Cleaning)
admin.site.register(Sail)
admin.site.register(Photo)