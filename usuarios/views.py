from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Events, Guests
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now
from django.http import Http404

# Create your views here.

@login_required
def home(request):
    events_list = Events.objects.all().order_by("-date").filter(user=request.user)

    Events.objects.filter(date__lt=now()).delete()

    paginator = Paginator(events_list, 3)
    page = request.GET.get("page")
    events = paginator.get_page(page)

    if request.method == "GET":
        return render(request, "home.html", {"events": events})

    elif request.method == "POST":
        title = request.POST.get("title-role")
        description = request.POST.get("description")
        date = request.POST.get("date-role")
        location = request.POST.get("location")

        if not title or not description or not date or not location:
            messages.error(request, "Todos os campos devem ser preenchidos!")
            return render(request, "home.html", {"events": events})

        try:
            event_date = datetime.fromisoformat(date)
            if event_date < datetime.now():
                messages.error(request, "A data não pode ser no passado!")
                return render(request, "home.html", {"events": events})
        except ValueError:
            messages.error(request, "Data inválida!")
            return render(request, "home.html", {"events": events})

        event = Events(
            title=title,
            description=description,
            date=event_date,
            location=location,
            user=request.user
        )
        
        event.save()
        return redirect("home")

       

@login_required 
def cancel_event(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Events, id=event_id)
        event.status = "Cancelado" 
        event.save()
        return JsonResponse({"status": "success", "message": "Evento cancelado com sucesso"})


@login_required
def view_event_by_id(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    guests = Guests.objects.filter(event=event)

    if event.user != request.user:
        messages.error(request, "Você não tem permissão para acessar este evento.")
        return redirect("home")

    if request.method == "GET":
        return render(request, "event.html", {"event": event, "guests": guests})
    elif request.method == "POST":
        name = request.POST.get("guest-name")
        whatsapp = request.POST.get("guest-wpp")
        max_companion = request.POST.get("guest-companion")

        if not name or not whatsapp:
            messages.error(request, "Todos os campos devem ser preenchidos!")
            return render(request, "event.html", {"event": event, "guests": guests})
        
        if not max_companion:
            max_companion = 0
        
        guest = Guests(
            event= event,
            name=name,
            whatsapp=whatsapp,
            max_companion= max_companion
        )

        guest.save()

        return redirect("view_event", event_id=event.id)
        