from . import views
from django.urls import path

urlpatterns = [
    path('', views.booking_view, name='booking'),
    path('booking_list/', views.booking_list_view, name='booking_list'),
    path('booking_list/edit_booking/<int:booking_id>',
         views.booking_edit, name='booking_edit'),
    path('booking_list/delete_booking/<int:booking_id>',
         views.booking_delete, name='booking_delete'),
]