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

    - GET /api/appointments/slots/?date=YYYY-MM-DD - Get available slots for a date.

    - POST /api/appointments/book/ - Book an appointment.