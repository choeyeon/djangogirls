

import uuid
from django.contrib.auth.models import AbstractUser
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
    image = models.ImageField()
    bank = models.CharField(max_length=100)
    type_user = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    email = models.EmailField(unique=True)

    
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
    text = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.CharField(max_length=2)
    date = models.DateField()


class EventImage(models.Model):
    image = models.ImageField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
























