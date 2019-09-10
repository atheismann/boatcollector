from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('boats/', views.boats_index, name='index'),
  path('boats/<int:boat_id>/', views.boat_detail, name='detail'),
  path('boats/create/', views.BoatCreate.as_view(), name='boats_create'),
  path('boats/<int:pk>/update/', views.BoatUpdate.as_view(), name='boats_update'),
  path('boats/<int:pk>/delete/', views.BoatDelete.as_view(), name='boats_delete'),
  path('boats/<int:boat_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
]