from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import Booking, Allergen
from .forms import BookingForm

# Create your views here.
class MakeBooking(generic.TemplateView):
    template_name = "booking/booking.html"

def booking_view(request):
    context ={}
    context['form']= BookingForm()
    return render(request, "booking.html", context)