from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import Booking, Allergen
from .forms import BookingForm

# Create your views here.
def booking_view(request):
    booking_form = BookingForm()

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.add_message(request, messages.SUCCESS, "Booking Successful! We look forward to seeing you!")


    return render(
        request,
        "booking/booking.html",
        {   
            "booking": Booking,
            "booking_form": booking_form
        },
    )