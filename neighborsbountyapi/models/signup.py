from django.db import models
from .event import Event
from .user import User


class SignUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE) 
    


class Meta:
        unique_together = ('user', 'event') 

def __str__(self):
        return f"{self.user.name} signed up for {self.event}"
