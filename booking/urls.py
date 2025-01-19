from . import views
from django.urls import path

urlpatterns = [
    path('', views.MakeBooking.as_view(), name='booking'),
]