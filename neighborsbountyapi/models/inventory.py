from django.db import models
from .event import Event


class Inventory(models.Model):
    foodType = models.CharField(max_length= 500)
    quantity = models.IntegerField(default=1, blank=True)
    pickupDate= models.DateField(blank=True)
    pickupLocation = models.CharField(max_length= 200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
