from django.contrib import admin
from .models import MenuItem

# Register your models here.
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'description')
    search_fields = ['name', 'category', 'allergens']
    list_filter = ('category', 'allergens',)
    filter_horizontal = ('allergens',)
