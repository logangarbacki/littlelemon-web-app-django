# Little Lemon Restaurant API

Live: https://littlelemon-web-app-django-production.up.railway.app/

REST API backend for the Little Lemon restaurant, built as the capstone for the Meta Back-End Developer Professional Certificate. Powers the React front-end with menu management, table bookings, and user authentication.

## Tech Stack

- Python 3.13 / Django 6
- Django REST Framework
- Djoser (token authentication)
- MySQL (Railway managed)
- Deployed on Railway with Gunicorn + WhiteNoise

## Features

- **Menu API** — full CRUD with category, featured flag, and image URL support
- **Featured Items** — filter endpoint (`?featured=true`) powers the home page specials
- **Bookings API** — table reservation creation (public) and management (authenticated)
- **Token Auth** — register, login, logout via Djoser
- **CORS** — configured to accept requests from the Vercel front-end
- **Django Admin** — full content management at `/admin/`
- **17 unit tests** — covering models and API endpoints

## API Endpoints

**Auth**
```
POST /auth/users/           — register a new user
POST /auth/token/login/     — obtain auth token
POST /auth/token/logout/    — revoke auth token
```

**Menu**
```
GET    /api/menu/           — list all menu items (public)
GET    /api/menu/?featured=true  — list featured/specials (public)
POST   /api/menu/           — create a menu item (auth required)
GET    /api/menu/<id>/      — retrieve a menu item (auth required)
PUT    /api/menu/<id>/      — update a menu item (auth required)
DELETE /api/menu/<id>/      — delete a menu item (auth required)
```

**Bookings**
```
POST   /api/bookings/       — create a booking (public)
GET    /api/bookings/       — list all bookings (auth required)
GET    /api/bookings/<id>/  — retrieve a booking (auth required)
PUT    /api/bookings/<id>/  — update a booking (auth required)
DELETE /api/bookings/<id>/  — delete a booking (auth required)
```

Authenticated endpoints require:
```
Authorization: Token <your_token>
```

## MenuItem Fields

| Field | Type | Notes |
|-------|------|-------|
| title | string | |
| price | decimal | |
| inventory | integer | |
| category | choice | Starters, Mains, Desserts, Drinks |
| image_url | url | optional, used by front-end |
| featured | boolean | surfaces item as a weekly special |

## Local Setup

```bash
pip install -r requirements.txt
```

Set database credentials in `littlelemon/settings.py` or via environment variables:

```
MYSQLDATABASE=littlelemon
MYSQLUSER=root
MYSQLPASSWORD=yourpassword
MYSQLHOST=127.0.0.1
MYSQLPORT=3306
```

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Tests

```bash
python manage.py test restaurant
```

## Front-End

React front-end that consumes this API:
https://github.com/logangarbacki/meta-front-end-developer-capstone

## Project Background

Built as the capstone for the Meta Back-End Developer Professional Certificate on Coursera.
https://www.coursera.org/professional-certificates/meta-back-end-developer
