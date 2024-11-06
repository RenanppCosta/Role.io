from datetime import datetime
from django.shortcuts import render
from .models import Events

# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method == "POST":
        title = request.POST.get("title-role")
        description = request.POST.get("description")
        date = request.POST.get("date-role")
        location = request.POST.get("location")

        event_date = datetime.fromisoformat(date)

        if event_date < datetime.now():
            return render(request, "home.html")
        
        event = Events(
            title=title,
            description=description,
            date=event_date,
            location=location
        )
        
        event.save()

        return render(request, "home.html")