web: gunicorn GitCommitter.wsgi:application --log-file -
web: python manage.py collectstatic --no-input;    
manage.py migrate