from django.db import models


class Member(models.Model):

    uid = models.IntegerField(default=1, blank=True)
    name = models.CharField(max_length=50)
