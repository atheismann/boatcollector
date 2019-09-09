from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('boats/', views.boats_index, name='index'),
  path('boats/<int:boat_id>/', views.boat_detail, name='detail'),
]