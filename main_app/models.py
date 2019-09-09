from django.db import models

# Create your models here.
class Boat(models.Model):
  name = models.CharField(max_length=100)
  manufacturer = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  length = models.CharField(max_length=100)
  beam = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name