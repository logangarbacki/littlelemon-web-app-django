from rest_framework import serializers
from django.utils import timezone
from .models import MenuItem, Booking


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            'id', 'title', 'description', 'price',
            'inventory', 'category', 'image_url', 'featured', 'ordering',
        ]


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'name', 'no_of_guests', 'booking_date', 'status', 'created_at']
        read_only_fields = ['user', 'status', 'created_at']

    def validate_booking_date(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("Booking date must be in the future.")
        return value

    def validate(self, data):
        booking_date = data.get('booking_date')
        if booking_date:
            conflict = Booking.objects.filter(
                booking_date=booking_date,
                status__in=['pending', 'confirmed'],
            )
            if self.instance:
                conflict = conflict.exclude(pk=self.instance.pk)
            if conflict.exists():
                raise serializers.ValidationError(
                    {"booking_date": "This time slot is already taken. Please choose another."}
                )
        return data
