from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking, Allergen


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('name', 'date', 'time_slot')
    search_fields = ['name', 'date']
    list_filter = ('date', 'time_slot',)
    summernote_fields = ('booking_notes')
    filter_horizontal = ('allergies',)


@admin.register(Allergen)
class AllergenAdmin(SummernoteModelAdmin):

    search_fields = ['name']
