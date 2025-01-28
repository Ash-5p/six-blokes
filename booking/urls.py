from . import views
from django.urls import path

urlpatterns = [
    path('', views.booking_view, name='booking'),
    path('booking_list/', views.booking_list_view, name='booking_list')
]