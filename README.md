# Little Lemon Restaurant API

Back-end REST API for the Little Lemon restaurant, built as the capstone project for the Meta Back-End Developer certificate. Designed to serve as the backend for a front-end client — handles menu management, table bookings, and user authentication.

Built with Django REST Framework, connected to a MySQL database.

## Stack

- Python / Django 6
- Django REST Framework
- Djoser (token authentication)
- MySQL

## What's included

- Menu API — full CRUD for restaurant menu items
- Booking API — full CRUD for table reservations
- Token-based user registration and authentication
- Unit tests for models and API endpoints (17 tests)

## API Endpoints

**Auth**
```
POST /auth/users/           — register a new user
POST /auth/token/login/     — obtain auth token
POST /auth/token/logout/    — revoke auth token
```

**Menu**
```
GET    /api/menu/           — list all menu items
POST   /api/menu/           — create a menu item
GET    /api/menu/<id>/      — retrieve a menu item
PUT    /api/menu/<id>/      — update a menu item
DELETE /api/menu/<id>/      — delete a menu item
```

**Bookings**
```
GET    /api/bookings/       — list all bookings
POST   /api/bookings/       — create a booking
GET    /api/bookings/<id>/  — retrieve a booking
PUT    /api/bookings/<id>/  — update a booking
DELETE /api/bookings/<id>/  — delete a booking
```

All `/api/` endpoints require a token header:
```
Authorization: Token <your_token>
```

## Setup

```bash
pip install -r requirements.txt
```

Update the database credentials in `littlelemon/settings.py`, then:

```bash
python manage.py migrate
python manage.py runserver
```

## Tests

```bash
python manage.py test restaurant
```
