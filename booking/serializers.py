from rest_framework import serializers
from datetime import date

from .models import Appointment
from django.core.validators import RegexValidator, MinLengthValidator


class AppointmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        validators=[
            MinLengthValidator(3, message="name should be at least 3 characters."),
            RegexValidator(
                regex=r"^[a-zA-Z\s]+$",
                message="first name should only contain letters",
            ),
        ],
    )
    phone_number = serializers.CharField(
        required=True,
        validators=[
            RegexValidator(
                regex=r"^\d{10}$", message="Please Enter a valid Mobile Number"
            )
        ],
    )

    class Meta:
        model = Appointment
        fields = ["id", "name", "phone_number", "date", "time_slot"]

    def validate(self, data):
        today = date.today()
        if data["date"] < today:
            raise serializers.ValidationError("You cannot book an appointment in the past.")
        
        if Appointment.objects.filter(
            date=data["date"], time_slot=data["time_slot"]
        ).exists():
            raise serializers.ValidationError("This slot is already booked.")
        return data
