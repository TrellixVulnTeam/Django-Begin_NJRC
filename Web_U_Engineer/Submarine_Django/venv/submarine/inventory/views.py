from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(reqeust):
    return HttpResponse('<h1>Hello Submarine</h1>')