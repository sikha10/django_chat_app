from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)

class Massage(models.Model):
    value = models.CharField(max_length=100000, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000, null=True)
    room = models.CharField(max_length=100000, null=True)

