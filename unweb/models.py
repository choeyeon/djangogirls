from types import ClassMethodDescriptorType
from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    
    currency = [
        (1, 'RUB')
        (2, 'UAN')
        (3, 'EUR')
        (4, 'USD')
    ]

    
    title = models.CharField(max_length=20)
    price = models.CharField(max_length=3, choices=currency, default=1)
    info = models.CharField(max_length=50, help_text='short description')
    description = models.TextField(max_length=500)



    def __str__(self):  
        return self.title




class Categories(models.Model):

    categories = models.CharField(max_length=30)






class Event(models.Model):
    
    title = models.CharField(max_length=50)
    info = models.TextField(max_length=300)
    requrement = models.CharField(max_length=50)
    location = models.ImageField()
    organizer = models.CharField()



    def __str__(self):  
        return self.title









class UserReg(models.Model):

    profile_photo = models.ImageField(upload_to ='', null=True, blank=True)
    firstname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=40)




class Profile(models.Model):

    photo = models.ImageField()
    name = models.CharField(max_length=100)







class AddNewEvent(models.Model):
    ...














    

    






















