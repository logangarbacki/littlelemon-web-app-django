from django.contrib import admin
from .models import MenuItem, Booking


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'featured', 'inventory', 'ordering')
    list_filter = ('category', 'featured')
    search_fields = ('title', 'description')
    list_editable = ('featured', 'ordering', 'price')
    ordering = ('ordering', 'title')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'booking_date', 'no_of_guests', 'status', 'user', 'created_at')
    list_filter = ('status', 'booking_date')
    search_fields = ('name', 'user__username')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'user')
    ordering = ('-booking_date',)
