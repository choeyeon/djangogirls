from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse


class service(models.Model):

    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'
    UAN = 'UAN'
    CURRENCY = (
        (RUB, 'RUB'),
        (USD, 'USD'),
        (EUR, 'EUR'),
        (UAN, 'UAN'),
    )

    title = models.CharField(max_length=20,)
    price = models.CharField(max_length=3, choices=CURRENCY, default=RUB,)
    info = models.CharField(max_length=50, help_text='short description')
    description = models.TextField(max_length=500,)



    def __str__(self):  

        return self.title

    
    def get_absolute_url(self):

        return reverse('service-detail', args=[str(self.id)])





        
