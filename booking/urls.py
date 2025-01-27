from . import views
from django.urls import path

urlpatterns = [
    path('', views.booking_view, name='booking'),
    # path('', view.booking_list_view, name='booking_list')
]