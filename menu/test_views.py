from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from booking.models import Allergen
from .models import MenuItem


class TestMenuViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@testcase.com"
        )
        self.allergen = Allergen.objects.create(name="test-allergen")
        self.menu = MenuItem.objects.create(
            name="test-name",
            category='starter',
            description="test-description"
        )
        self.menu.allergens.set([self.allergen])

    def test_successful_render_menu_item(self):
        """Test for viewing a menu item"""
        response = self.client.post(reverse(
            'menu'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'test-name', response.content)
        self.assertIn(b'test-allergen', response.content)
        self.assertIn(b'test-description', response.content)
