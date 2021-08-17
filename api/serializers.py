from django.db import models
from api.models import Category, Event, Event, EventImage, Review, Ticket, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['image', 'bank', 'type_user', 'email', 'phone']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['__all__']


class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = ['__all__']
    

class RevievSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['__all__']
        


class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ['__all__']


class EventImageSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = EventImage
        fields = ['__all__']


class EventDateSerializer(serializers.ModelSerializer):
    ...