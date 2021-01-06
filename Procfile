release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn Django_Test.wsgi --log-file -