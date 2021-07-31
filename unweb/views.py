from django.shortcuts import render
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login
from .forms import LoginForm


#TODO доробити варiанти 
def login_user(rquest):

    if request.method == 'POST':
        form = LoginForm(request.POST)





