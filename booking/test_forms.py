from datetime import date
from django.test import TestCase
from .models import Allergen
from .forms import BookingForm


class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        """Tests if booking form is valid"""
        test_allergen = Allergen.objects.create(name="Test")
        booking_form = BookingForm(
            {'date': date.today().strftime("%Y-%m-%d"),
             'time_slot': 16,
             'guests': 2,
             'allergies': [test_allergen.id],
             'booking_notes': 'Test'
             })
        self.assertTrue(booking_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        """Tests if booking form is invalid"""
        test_allergen = Allergen.objects.create(name="Test")
        booking_form = BookingForm(
            {'date': date.today().strftime("%Y-%m-%d"),
             'time_slot': 16,
             'guests': 13,
             'allergies': [test_allergen.id],
             'booking_notes': 'Test'
             })
        self.assertFalse(booking_form.is_valid(), msg='Form is valid')
