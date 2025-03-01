from allauth.account.forms import LoginForm
from django.urls import reverse
from django.test import TestCase
from users.forms import CustomSignupForm


class TestSigninSignupViews(TestCase):

    def test_successful_custom_signup_form_render(self):
        """Test for ensuring signin & signup forms render correctly"""
        response = self.client.get(reverse(
            'signin_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('login_form', response.context)
        self.assertIn('signup_form', response.context)
        self.assertIsInstance(response.context['login_form'], LoginForm)
        self.assertIsInstance(
            response.context['signup_form'], CustomSignupForm)
