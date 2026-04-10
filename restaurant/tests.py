from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from datetime import datetime
from .models import MenuItem, Booking


class MenuItemModelTest(TestCase):
    def setUp(self):
        self.item = MenuItem.objects.create(
            title='Greek Salad',
            price=12.99,
            inventory=50
        )

    def test_menu_item_str(self):
        self.assertEqual(str(self.item), 'Greek Salad')

    def test_menu_item_price(self):
        self.assertEqual(self.item.price, 12.99)

    def test_menu_item_inventory(self):
        self.assertEqual(self.item.inventory, 50)


class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name='John Doe',
            no_of_guests=4,
            booking_date=datetime(2026, 6, 15, 19, 0)
        )

    def test_booking_str(self):
        self.assertEqual(str(self.booking), 'John Doe')

    def test_booking_guests(self):
        self.assertEqual(self.booking.no_of_guests, 4)


class MenuItemAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.item = MenuItem.objects.create(
            title='Bruschetta',
            price=8.50,
            inventory=30
        )

    def test_get_menu_items(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_item(self):
        data = {'title': 'Lemon Dessert', 'price': 6.99, 'inventory': 20}
        response = self.client.post('/api/menu/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_menu_item(self):
        response = self.client.get(f'/api/menu/{self.item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Bruschetta')

    def test_update_menu_item(self):
        data = {'title': 'Bruschetta', 'price': 9.00, 'inventory': 25}
        response = self.client.put(f'/api/menu/{self.item.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data['price']), 9.00)

    def test_delete_menu_item(self):
        response = self.client.delete(f'/api/menu/{self.item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthenticated_request_rejected(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class BookingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.booking = Booking.objects.create(
            name='Jane Smith',
            no_of_guests=2,
            booking_date=datetime(2026, 7, 20, 18, 30)
        )

    def test_get_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_booking(self):
        data = {
            'name': 'Alice Johnson',
            'no_of_guests': 3,
            'booking_date': '2026-08-01T19:00:00Z'
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_booking(self):
        response = self.client.get(f'/api/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Jane Smith')

    def test_update_booking(self):
        data = {
            'name': 'Jane Smith',
            'no_of_guests': 5,
            'booking_date': '2026-07-20T18:30:00Z'
        }
        response = self.client.put(f'/api/bookings/{self.booking.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['no_of_guests'], 5)

    def test_delete_booking(self):
        response = self.client.delete(f'/api/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthenticated_request_rejected(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
