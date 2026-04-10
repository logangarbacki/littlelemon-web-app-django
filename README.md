# Little Lemon Restaurant - Back-end Capstone

This is the back-end capstone project for the Meta Back-End Developer certificate. Built a REST API for the Little Lemon restaurant using Django and Django REST Framework, connected to a MySQL database.

## What's built

- Menu API — full CRUD for restaurant menu items
- Booking API — full CRUD for table reservations
- User registration and token-based authentication via Djoser
- Static HTML page served by Django
- Unit tests for models and API endpoints
- MySQL database backend

## API Paths

**Auth**
- `POST /auth/users/` — register
- `POST /auth/token/login/` — get token
- `POST /auth/token/logout/` — revoke token

**Menu**
- `GET/POST /api/menu/`
- `GET/PUT/DELETE /api/menu/<id>/`

**Bookings**
- `GET/POST /api/bookings/`
- `GET/PUT/DELETE /api/bookings/<id>/`

## Setup

```bash
pip install -r requirements.txt
# update MySQL credentials in littlelemon/settings.py
python manage.py migrate
python manage.py runserver
```

## Testing

```bash
python manage.py test restaurant
```

All requests to `/api/` require a token in the header:
```
Authorization: Token <your_token>
```
