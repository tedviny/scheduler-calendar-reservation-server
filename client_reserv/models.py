from django.db import models


# Create your models here.
from django.utils.text import slugify


class Reservation(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    TimeSlot = models.CharField(max_length=255)

    class Meta:
        ordering = ['TimeSlot']

    def __str__(self):
        return self.TimeSlot


class TimeSlot(models.Model):
    TimeSlot = models.CharField(max_length=255)

    class Meta:
        ordering = ['TimeSlot']

    def __str__(self):
        return self.TimeSlot
