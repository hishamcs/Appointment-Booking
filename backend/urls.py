from django.contrib import admin
from django.urls import path, include
from booking.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/appointments/", include("booking.urls")),
    path("", home, name='home-page'),
]
