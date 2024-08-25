from django.db import models
from .eventtype import EventType



class Event(models.Model):
    eventDate = models.DateField()
    eventType = models.ForeignKey(EventType, on_delete=models.CASCADE)
    location = models.CharField(max_length = 100)
    eventTime = models.TimeField()
    
    def __str__(self):
        return f"{self.eventType} on {self.eventDate} at {self.location}"
