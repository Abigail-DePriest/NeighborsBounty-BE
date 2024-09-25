from django.db import models
from django.utils import timezone

class Inventory(models.Model):
    weekStartDate = models.DateField(default=timezone.now)
    weekEndDate = models.DateField(default=timezone.now)
    pickupLocation = models.CharField(max_length=200, blank=True, default='Unknown')
    items = models.JSONField(default=list)  # Store items as a JSON object

    def __str__(self):
        return f"Inventory from {self.weekStartDate} to {self.weekEndDate}"
