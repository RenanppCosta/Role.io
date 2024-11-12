from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("cancel-event/<int:event_id>/", views.cancel_event, name="cancel-event")
]
