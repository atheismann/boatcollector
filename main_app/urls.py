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
  path('boats/<int:boat_id>/add_photo/', views.add_photo, name='add_photo'),
  path('boats/<int:boat_id>/assoc_sail/<int:sail_id>/', views.assoc_sail, name='assoc_sail'),
  path('boats/<int:boat_id>/unassoc_sail/<int:sail_id>/', views.unassoc_sail, name='unassoc_sail'),
  path('sails/', views.SailList.as_view(), name='sails_index'),
  path('sails/<int:pk>/', views.SailDetail.as_view(), name='sails_detail'),
  path('sails/create/', views.SailCreate.as_view(), name='sails_create'),
  path('sails/<int:pk>/update/', views.SailUpdate.as_view(), name='sails_update'),
  path('sails/<int:pk>/delete/', views.SailDelete.as_view(), name='sails_delete'),
]