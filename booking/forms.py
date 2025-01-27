from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'time_slot', 'guests', 'allergies', 'booking_notes')