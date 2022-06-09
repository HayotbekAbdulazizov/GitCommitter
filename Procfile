web: gunicorn GitCommitter.wsgi:application --log-file -
python manage.py collectstatic --noinput
manage.py migrate