from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.utils.dateparse import parse_date


from .models import Appointment
from .serializers import AppointmentSerializer


class AvailableSlotsView(APIView):
    TIME_SLOTS = [
        "10:00 AM",
        "10:30 AM",
        "11:00 AM",
        "11:30 AM",
        "12:00 PM",
        "12:30 PM",  # Skip 1:00 PM - 2:00 PM
        "2:00 PM",
        "2:30 PM",
        "3:00 PM",
        "3:30 PM",
        "4:00 PM",
        "4:30 PM",
    ]

    def get(self, request, *args, **kwargs):
        date = request.query_params.get("date")
        if not date:
            return Response(
                {"error": "Date parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        date_obj = parse_date(date)
        print(date_obj)
        print(date_obj)
        if not date_obj:
            return Response(
                {"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Get booked slots for the date
        booked_slots = set(
            Appointment.objects.filter(date=date_obj).values_list(
                "time_slot", flat=True
            )
        )

        # Filter available slots
        available_slots = [slot for slot in self.TIME_SLOTS if slot not in booked_slots]

        return Response(
            {"date": date, "available_slots": available_slots},
            status=status.HTTP_200_OK,
        )


class BookAppointmentView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


def home(reqeust):
    return render(reqeust, "index.html")
