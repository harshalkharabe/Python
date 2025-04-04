from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    s = "<h1>Hello, Django!<h1>"
    return HttpResponse(s)

def time(request):
    import datetime
    now = datetime.datetime.now()
    s = f"<h1>Current Date and Time: {now}</h1>"
    return HttpResponse(s)