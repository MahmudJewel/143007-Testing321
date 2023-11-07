from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_homepage(request):
    return HttpResponse("Hello, world. You're at the polls index.")