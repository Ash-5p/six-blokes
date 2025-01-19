from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'date', 'time_slot', 'guests', 'allergies', 'booking_notes')