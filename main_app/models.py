from django.db import models
from django.urls import reverse
from datetime import date

CLEANINGS = (
  ('H', 'Hull'),
  ('D', 'Deck'),
  ('I', 'Interior'),
)

# Create your models here.
class Sail(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sails_detail', kwargs={'pk': self.id})
    
class Boat(models.Model):
  name = models.CharField(max_length=100)
  manufacturer = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  length = models.CharField(max_length=100)
  beam = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=250)
  sails = models.ManyToManyField(Sail)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'boat_id': self.id})

  def cleaned_recently(self):
    return self.cleaning_set.filter(date=date.today()).count() >= len(CLEANINGS)

class Cleaning(models.Model):
  date = models.DateField('feeding date')
  cleaning = models.CharField(
    max_length=1,
    choices=CLEANINGS,
    default=CLEANINGS[0][0],
  )

  boat = models.ForeignKey(Boat, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_cleaning_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  boat = models.ForeignKey(Boat, on_delete=models.CASCADE)

  def __str__(self):
      return f"Photo for boat_id: {self.boat_id} @{self.url}"