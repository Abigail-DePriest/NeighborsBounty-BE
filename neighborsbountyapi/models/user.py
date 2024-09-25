from django.db import models
from .event import Event


class User(models.Model):

    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    events = models.ManyToManyField(Event, through='Signup', related_name='users')
