from rest_framework import permissions
from api import models
from api.models import User, Review
from django.shortcuts import render
from django.http import HttpResponse, request, response
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from . import serializers
from django.http import JsonResponse
import random
from rest_framework import viewsets
from api.serializers import RevievSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics
from rest_framework.mixins import Mixin, UpdateModelMixin


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
    queryset = models.Review.objects.all()
    serializer_class = RevievSerializer
    permissions_classes = ()

    def list(self, request, *args, **kwargs):
        user = self.get_object()
        queryset = self










