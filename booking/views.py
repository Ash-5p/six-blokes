from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import Booking, Allergen
from .forms import BookingForm

# Create your views here.
class MakeBooking(generic.FormView):
    queryset = Booking.objects.all()
    template_name = "booking_form.html"