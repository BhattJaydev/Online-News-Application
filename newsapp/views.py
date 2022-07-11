import requests
from django.shortcuts import render
from requests import *

from newsapp.models import Contact


def about(request):
    return render(request, 'about.html')

def contact(request):
    # fn = request.POST['fn']
    # ln = request.POST['ln']
    # ct = request.POST['ct']
    # mail = request.POST['mail']
    # ph = request.POST['ph']
    # contact = Contact.objects.create(first_name=fn, last_name=ln, country=ct, email=mail,ph=ph)
    # contact.save()
    return render(request, 'contact.html')



def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def home(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)

def india(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=national")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)

def world(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=world")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)

def bussiness(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=business")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)

def politics(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=politics")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)

def technology(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=technology")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)

def science(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=science")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)

def automobile(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=automobile")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)


def entertainment(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=entertainment")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)


def sports(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=sports")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)

def startups(request):
    records = {}
    url = requests.get("https://inshortsapi.vercel.app/news?category=startup")
    inshorts_data = url.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'page.html',records)

