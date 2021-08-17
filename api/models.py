
import datetime
import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.forms.fields import ImageField
from django.utils.translation import ugettext_lazy as _
#from phonenumber_field.modelfields import PhoneNumberField
from types import ClassMethodDescriptorType
from django.db import models
from django.db.models.fields import CharField, DateField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models

class User(AbstractUser):
    TYPES =(
        (1, 'common')
        (2, 'advanced')
        (3, 'eventmaker')
    )

    image = models.ImageField(blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True)
    type_user = models.CharField(max_length=10, choices=TYPES, default=1)
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = ImageField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=50)
    descriptin = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_verified = models.BooleanField(True)
    price = models.FloatField(blank=False)
    location = models.PointField(null=True, blank=True )

    def __str__(self):
        return self.title


class Review(models.Model):
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    text = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING)

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.CharField(max_length=2)
    date = models.DateField()


class EventImage(models.Model):
    image = models.ImageField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class EventDate(models.Model):    
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    length = models.IntegerField()


    def save(self, *args, **kwargs):
        start = datetime.combine(self.date, self.time)
        duration = self.length

        self.event.start = start
        self.event.end = start + duration
        self.event.save()


class RecurringEvents(models.Model):
    event = models.OneToOneField(Event, on_delete=CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class EveryWeekEvents(models.Model):
    DAY = (
        (1, 'Monday')
        (2, 'Tuesday')
        (3, 'Wednesday')
        (4, 'Thursday')
        (5, 'Friday')
        (6, 'Saturday')
        (7, 'Sunday')
    )

    event = models.OneToOneField(Event, on_delete=CASCADE)
    start_event = models.IntegerField(choices=DAY)
    start_time = models.TimeField()
    end_time = models.TimeField()
    


    
   























