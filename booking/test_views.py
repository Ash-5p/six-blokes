from datetime import date
import json
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Booking, Allergen


class TestBookingViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@testcase.com"
        )
        self.allergen = Allergen.objects.create(name="Test")
        self.booking = Booking.objects.create(
            user=self.user,
            date=date.today().strftime("%Y-%m-%d"),
            time_slot=16,
            guests=1,
            booking_notes="Test"
        )
        self.booking.allergies.set([self.allergen])

    def test_successful_booking_submission(self):
        """Test for creating a booking"""
        self.client.login(
            username="myUsername", password="myPassword")
        response = self.client.post(reverse(
            'booking_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            b'You currently have no upcoming bookings',
            response.content
        )

    def test_booking_edit_modal_renders_booking_information(self):
        """Test to see if booking information renders in the edit modal"""
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse(
            'booking_edit', args=[self.booking.id]
            ))
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)

        self.assertEqual(
            response_data["date"], date.today().strftime("%Y-%m-%d")
            )
        self.assertEqual(response_data["time_slot"], 16)
        self.assertEqual(response_data["guests"], 1)
        self.assertEqual(response_data["booking_notes"], "Test")
        self.assertIn(self.allergen.id, response_data["allergies"])
