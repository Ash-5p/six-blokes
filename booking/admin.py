from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking ,Allergen

# Register your models here.
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('name', 'date', 'timeSlot')
    search_fields = ['name', 'date']
    list_filter = ('date', 'timeSlot',)
    summernote_fields = ('bookingNotes')


# Register your models here.
@admin.register(Allergen)
class AllergenAdmin(SummernoteModelAdmin):

    search_fields = ['name']
