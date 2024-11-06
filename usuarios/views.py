from datetime import datetime
from django.shortcuts import render, redirect
from .models import Events

# Create your views here.

def home(request):
    if request.method == "GET":
        events = Events.objects.all()

        return render(request, "home.html", {"events": events})
    
    elif request.method == "POST":
        title = request.POST.get("title-role")
        description = request.POST.get("description")
        date = request.POST.get("date-role")
        location = request.POST.get("location")
        
        if date:
            event_date = datetime.fromisoformat(date)
            if event_date < datetime.now():
                return render(request, "home.html")
        else:
            return render(request, "home.html")
        
            
        event = Events(
            title=title,
            description=description,
            date=event_date,
            location=location
        )
        
        event.save()

        return redirect("home")