from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def landing(request):
    return HttpResponse('<h1>Hello</h1>')
