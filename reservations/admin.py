from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'guests')  # This will show these fields in the admin list view
    search_fields = ('name', 'email', 'phone')  # Allows you to search by these fields
    list_filter = ('date', 'guests')  # Adds filter options in the right-hand sidebar
