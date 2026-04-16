from django.db import models
from django.contrib.auth.models import User
import json


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Starters', 'Starters'),
        ('Mains', 'Mains'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Mains')
    image_url = models.URLField(blank=True, default='')
    featured = models.BooleanField(default=False)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['ordering', 'title']

    def __str__(self):
        return self.title


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bookings',
    )
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-booking_date']

    def __str__(self):
        return f"{self.name} — {self.booking_date.strftime('%Y-%m-%d %H:%M')}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('preparing', 'Preparing'),
        ('on_the_way', 'On the Way'),
        ('delivered', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_number = models.IntegerField(unique=True)
    items = models.JSONField(default=list)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, default=3.99)
    tip = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    address = models.CharField(max_length=500)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparing')
    eta = models.IntegerField(default=30)
    placed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-placed_at']

    def __str__(self):
        return f"Order #{self.order_number} — {self.user}"
