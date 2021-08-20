from django.contrib.gis.db.models.fields import PointField
from django.db import models
from api.models import Category, Event, Event, EventDate, EventImage, Review, Ticket, User
from rest_framework import serializers



class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    username = serializers.CharField()


    class Meta:
        models = User
        fields = ('phone', 'image', 'full_name', 'event', 'review')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer

    class Meta:
        model = User
        fields = ['__all__']
        extra_kworgs = {'password': {'write_only': True}}


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['__all__']


class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    user = UserSerializer(many = True)
    
    class Meta:
        model = Event
        fields = ['__all__']
        extra_kwargs = {
            'price': {'read_only': True},
        }
    

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
        extra_kwargs = {
            'price': {'read_only': True},
        }


class EventImageSerializer(serializers.ModelSerializer):
    event = EventSerializer(write_only=True)

    class Meta:
        model = EventImage
        fields = ['__all__']


class EveryWeekEventSerializer(serializers.ModelSerializer):
    DAY = (
        (1, 'monday'),
        (2, 'tuesday'),
        (3, 'wednesday'),
        (4, 'thursday'),
        (5, 'friday'),
        (6, 'saturday'),
        (7, 'sunday')
    )

    start_event = serializers.ChoiceField(DAY)
    event = EventSerializer(read_only=True)


class ReccyringEventSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(write_only=True)
    end_date = serializers.DateField(write_only=True)

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("finish must occur after start")
        return data


class EventDateSerializrs(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    date = serializers.DateField(write_only=True)
    time = serializers.TimeField(write_only=True)
    
    class Meta:
        model = EventDate
        fields = ('length')


class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    username = serializers.CharField()


    class Meta:
        models = User
        fields = ('phone', 'image', 'full_name', 'event', 'review')


class EventListSerializer(serializers.ModelsSerializer):
    title = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    start = serializers.DateTimeField(read_only=True)
    image = serializers.ImageField(read_only=True)
    location = PointField(read_only=True)
    
    class Meta:
         models = Event
         fields = ('title', 'price', 'start', 'image', 'location')


class EventReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('text', 'rating',)



