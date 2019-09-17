from django.shortcuts import render
from django.http import HttpResponse

# Create your views here, views are web pages

def index(response):
    return HttpResponse("<h1>Welcome Page</h1>")

def view1(response):
	return HttpResponse("<h2>view 1</h2>")

