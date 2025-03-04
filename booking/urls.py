from django.urls import path

from .views import *


urlpatterns = [
    path("slots/", AvailableSlotsView.as_view(), name="available_slots"),
    path("book/", BookAppointmentView.as_view(), name="book_appointment"),
]
