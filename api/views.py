from django.shortcuts import render
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from . import serializers
from django.http import JsonResponse
import random
from django.contrib.auth.models import User
from rest_framework import generics







