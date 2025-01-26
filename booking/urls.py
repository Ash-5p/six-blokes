from . import views
from django.urls import path

urlpatterns = [
    path('', views.booking_view, name='booking'),
]