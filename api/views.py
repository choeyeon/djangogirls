from django.views.generic import GenericViewError
from rest_framework import permissions
from rest_framework import mixins
from api import models
from api.models import Event, User, Review
from django.http import HttpResponse, request, response
from rest_framework.views import APIView
from . import serializers
from django.http import JsonResponse
import random
from rest_framework import viewsets
from api.serializers import EventSerializer, ProfileSerializer, RevievSerializer, TicketSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics
from rest_framework.mixins import DestroyModelMixin, Mixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet



class UserVievSet(UpdateModelMixin):
    queryset = User.object.all()
    serilizer_class = UserSerializer
    permissions_clases = [IsAuthenticated]

    def get_queryset():
        return User.objects.all()


class UserListViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class ReviewVievSet(generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = RevievSerializer
    permissions_classes = ()

    def list(self, request, *args, **kwargs):
        user = self.get_object()
        queryset = self

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)


class EventVievSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, GenericViewSet):
    serializer_class = EventSerializer
    queryset = Event.object.all()
    permissions_clases = [IsAuthenticated]

    def crate(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class ProfileVievSet(mixins.UpdateModelMixin, GenericViewSet):
    queryset = User.object.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return User.objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class TicketVievSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = models.Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    









