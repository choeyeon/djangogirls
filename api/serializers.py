from django.db import models
from api.models import Category, Event, Event, EventImage, Review, Ticket
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['__all__']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


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
        


class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = Ticket


class EventImageSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = EventImage