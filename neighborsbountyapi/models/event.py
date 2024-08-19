from django.db import models


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
      ('gleaning', 'Gleaning'),
      ('cooking', 'Cooking'),
      ('distribution', 'Distribution')
    ]
    eventDate = models.DateField(blank=True)
    eventType = models.CharField(max_length = 55, choices=EVENT_TYPE_CHOICES, default= "gleaning")
    location = models.CharField(max_length = 100)
    eventTime = models.TimeField(blank=True)
