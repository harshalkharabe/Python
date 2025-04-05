from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def name(request):
    return HttpResponse("<h1>Welcome to the second app</h1>")