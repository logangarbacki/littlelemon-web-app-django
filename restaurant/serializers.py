from rest_framework import serializers
from django.utils import timezone
from .models import MenuItem, Booking, Order


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
        read_only_fields = ['user', 'created_at']

    def validate_status(self, value):
        if self.instance and value not in ['cancelled']:
            raise serializers.ValidationError("You can only cancel a booking.")
        return value

    def validate_booking_date(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("Booking date must be in the future.")
        return value

    def validate(self, data):
        if 'status' in data and len(data) == 1:
            return data
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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'items', 'subtotal', 'delivery_fee',
            'tip', 'discount', 'total', 'address', 'name', 'email',
            'status', 'eta', 'placed_at',
        ]
        read_only_fields = ['placed_at']
