Appointment Booking System

A simple appointment booking system built with Django REST Framework (DRF) and a JavaScript plugin for frontend integration.

Features

    - View available appointment slots
    - Book an appointment
    - Prevents double-booking
    - Embeddable JavaScript widget for easy integration

Requirements

    - Python 
    - Django
    - Django REST Framework

Installation & Setup


Clone the repository:

 https://github.com/hishamcs/Appointment-Booking.git
 

Create a virtual environment and activate it:

 python -m venv venv
 source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`

Install dependencies:

 pip install -r requirements.txt

Apply migrations and start the server:

     - python manage.py migrate
     - python manage.py runserver

Frontend (JavaScript Plugin)

    - Add the following script to your HTML file:

        <script src="http://127.0.0.1:8000/appointment-booking.js"></script>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                EmbedBookingWidget("booking-container");
            });
        </script>
        <div id="booking-container"></div>

API Endpoints

    1. GET /api/appointments/slots/?date=YYYY-MM-DD - Get available slots for a date.

        Request Example: GET /api/appointments/slots/?date=2025-03-10

        Response Example (Success - 200 OK):
            {
                "date": "2025-03-10",
                "available_slots": [
                    "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
                    "12:00 PM", "12:30 PM", "2:00 PM", "2:30 PM",
                    "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM"
                ]
            }

    2. POST /api/appointments/book/ - Book an appointment.

        Request Example:

        {
            "name": "John Doe",
            "phone_number": "1234567890",
            "date": "2025-03-10",
            "time_slot": "10:00 AM"
        }

        Response Example (Success - 201 Created):
            Success response 
        
        Response Example (Failure - 400 Bad Request - Slot Already Booked):
        {
            "error": "This slot is already booked."
        }