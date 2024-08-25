from django.db import models
from .event import Event
from .member import Member
from .role import Role

class SignUp(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE) 
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
