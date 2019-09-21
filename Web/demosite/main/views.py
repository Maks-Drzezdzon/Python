from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here, views are web pages

def index(response, id):
	ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h2>%s</h2>" % ls.name)

def view1(response):
	return HttpResponse("<h2>test 1</h2>")

