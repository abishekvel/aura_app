# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
    Device_id = models.CharField(max_length=100)
    Device_name = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)

    def __str__(self):
        return self.Device_id

class Task(models.Model):
    Device_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    Device_status = models.BooleanField(default=False)
    End_time = models.IntegerField(default=0)
    Start_time = models.IntegerField(default=0)

    def __str__(self):
        return self.Device_status
