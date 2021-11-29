web: gunicorn --pythonpath flight flight.wsgi
release: python flight/manage.py makemigrations
release: python flight/manage.py migrate