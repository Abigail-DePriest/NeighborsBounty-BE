from django.db import models
from .event import Event
from .member import Member

class SignUp(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE) 
