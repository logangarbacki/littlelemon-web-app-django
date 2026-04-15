release: python manage.py migrate --noinput && python manage.py seed_menu
web: python manage.py collectstatic --noinput && gunicorn littlelemon.wsgi
