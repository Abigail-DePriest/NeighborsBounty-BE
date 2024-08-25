from django.db import models


class EventType(models.Model):
  eventTypeName = models.CharField(max_length=20)
  
  
  def __str__(self):
        return self.eventTypeName
