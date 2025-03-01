from django.test import TestCase
from users.forms import CustomSignupForm


class TestSignupForm(TestCase):

    def test_custom_signup_form_is_valid(self):
        """Tests custom signup form is valid"""
        signup_form = CustomSignupForm(
            {'name': 'Test Name',
             'email': 'test@test.com',
             'password1': 'sixBlokes432',
             'password2': 'sixBlokes432'
             })
        self.assertTrue(signup_form.is_valid(), msg='Form is not valid')

    def test_custom_signup_form_is_invalid(self):
        """Tests custom signup form is valid"""
        signup_form = CustomSignupForm(
            {'name': '',
             'email': 'test@test.com',
             'password1': 'sixBlokes432',
             'password2': 'sixBlokes123'
             })
        self.assertFalse(signup_form.is_valid(), msg='Form is valid')
