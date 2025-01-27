from .models import Booking
from django import forms
from datetime import date


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'time_slot', 'guests', 'allergies', 'booking_notes')
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'min': date.today().strftime('%Y-%m-%d')  # Set the minimum date to today
                }
            ),
            'guests': forms.NumberInput(
                attrs={
                    'min': 1,
                    'max': 12,
                }
            ),
        }