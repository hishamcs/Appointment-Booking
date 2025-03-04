from django.db import models
from django.core.exceptions import ValidationError


class Appointment(models.Model):
    TIME_SLOTS = [
        ("10:00 AM", "10:00 AM"),
        ("10:30 AM", "10:30 AM"),
        ("11:00 AM", "11:00 AM"),
        ("11:30 AM", "11:30 AM"),
        ("12:00 PM", "12:00 PM"),
        ("12:30 PM", "12:30 PM"),
        ("2:00 PM", "2:00 PM"),
        ("2:30 PM", "2:30 PM"),
        ("3:00 PM", "3:00 PM"),
        ("3:30 PM", "3:30 PM"),
        ("4:00 PM", "4:00 PM"),
        ("4:30 PM", "4:30 PM"),
    ]

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time_slot = models.CharField(max_length=10, choices=TIME_SLOTS)

    class Meta:
        unique_together = ("date", "time_slot")

    def __str__(self):
        return f"{self.name} - {self.date} - {self.time_slot}"
