from django.urls import path
from .views import custom_logout_view

urlpatterns = [
    # Other URLs...
    path('accounts/logout/', custom_logout_view, name='account_logout'),  # Overrides Allauth logout
]