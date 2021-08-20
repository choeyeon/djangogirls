
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
        (1, 'common'),
        (2, 'advanced'),
        (3, 'eventmaker'),
    )

    image = models.ImageField(blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True)
    type_user = models.CharField(max_length=10, choices=TYPES, default=1)
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    event = models.ManyToManyField('Event', blank=True, related_name='+')
    review = models.ForeignKey('Review', blank=True, on_delete=CASCADE, related_name='+')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)

    
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = ImageField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=50)
    descriptin = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING)

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.CharField(max_length=2)
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

    def save(self, *args, **kwargs):
        self.event.start = self.start_date
        self.event.end = self.end_date
        self.event.save()
    


class EveryWeekEvents(models.Model):
    DAY = (
        (1, 'monday'),
        (2, 'tuesday'),
        (3, 'wednesday'),
        (4, 'thursday'),
        (5, 'friday'),
        (6, 'saturday'),
        (7, 'sunday')
    )

    event = models.OneToOneField(Event, on_delete=CASCADE)
    start_event = models.IntegerField(choices=DAY)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def save(self, *args, **kwargs):
        self.event.start_day = self.start_event
        self.event.time_start = self.start_time
        self.event.end = self.end_time
        self.event.save()
    

class UserManager(models.Manager):
    ...

    def create(self, username, image, type_user, email):
        user = User(username = username, image = image, type_user = type_user, email = email)
        user.save()
        profile = Profile()
        user = user
        profile.save()
        return user
   























