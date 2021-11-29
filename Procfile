web: gunicorn --pythonpath flight flight.wsgi
release: python companies/manage.py makemigrations
release: python companies/manage.py migrate