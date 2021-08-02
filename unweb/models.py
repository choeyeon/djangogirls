

import uuid
from django.db.models.fields.related import ForeignKey
from django.forms.fields import ImageField

from django.utils.translation import ugettext_lazy as _

#from phonenumber_field.modelfields import PhoneNumberField
from types import ClassMethodDescriptorType
from django.db import models
from django.db.models.fields import CharField, DateField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


    






class User (models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
    image = models.ImageField()
    is_superuser = models.BooleanField(null=True)
    bank = models.CharField(max_length=100)
    type_user = models.CharField(max_length=100)
    #phone = models.PhoneNumderField(null=False, blank=False, unique=True, help_text='phone number')
    phone_code = models.CharField(max_length=10)
    email = models.EmailField()
    id = models.AutoField(primary_key=True)






class Category(models.Model):
    name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)


class Review(models.Model):
    text = models.CharField(max_length=50)
    user_photo = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Ticket(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)









class MyEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)





class EventImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
























