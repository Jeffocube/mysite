import requests
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Post
# Create your views here.
def forum(request):#Forum page
    context = {#Put all posts onto the web page
        'posts': Post.objects.all()
    }
    return render(request, "forum.html", context)

def index(request):#Home page
    return render(request, "index.html")

def db(request):#View from earlier testing. Ignore
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})

def addforum(request):#Takes POST requests and saves to database
    titl = request.POST.get("title")
    conten = request.POST.get("content")
    p = Post(title=titl, content=conten)
    p.save()
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "forum.html", context)

def reg(request):#Allow for registration of users
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')#Get username from form for display
            messages.success(request, f'Account created for {username}!')
            return render(request, "index.html")
    else:
        form = UserRegisterForm()
    return render(request, "reg.html", {'form':form})

def getPosts(request):#Returns posts to forum page
    results = Post.objects.all()#Get all posts
    results_serialize= json.loads(serialize('json', results))
    return JsonResponse({'data': results_serialize})
