from datetime import date
from django import forms
from .models import Booking, Allergen


class BookingForm(forms.ModelForm):
    allergies = forms.ModelMultipleChoiceField(
        queryset=Allergen.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Booking
        fields = ('date', 'time_slot', 'guests', 'allergies', 'booking_notes')
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'min': date.today().strftime('%Y-%m-%d'),
                }
            ),
            'guests': forms.NumberInput(
                attrs={
                    'min': 1,
                    'max': 12,
                }
            ),
        }
