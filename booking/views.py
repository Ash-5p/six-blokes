from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
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
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking_form.save()
            messages.success(request, "Booking Successful! We look forward to seeing you!")
            return redirect(booking_list_view)
        else:
            messages.error(request, "Booking failed, Please try again")

    return render(
        request,
        "booking/booking.html",
        {   
            "booking": Booking,
            "booking_form": booking_form
        },
    )

# class BookingList(generic.ListView):
#     queryset = Booking.objects.all().order_by("-date")
#     template_name = "booking/booking_list.html"

def booking_list_view(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(
        request,
        "booking/booking_list.html",
        {"user_bookings": user_bookings}
    )