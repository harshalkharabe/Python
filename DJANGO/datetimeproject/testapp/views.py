from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def date_time(request):
    current_date = datetime.now()
    # Get only hours form current date
    hrs = int(current_date.strftime("%H"))
    message = "<h2>Hello, "
    if hrs < 12:
        message += "Good Morning!"
    elif hrs < 17:
        message += "Good Afternoon!"
    else:
        message += "Good Evening!"
    message += "</h2>"
    return HttpResponse(message)