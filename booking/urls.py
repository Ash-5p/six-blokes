from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookingForm.as_view(), name='home'),
]