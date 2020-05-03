release: python prerequisites.py
release: python manage.py migrate
web: gunicorn django_bookworm.wsgi --log-file -
