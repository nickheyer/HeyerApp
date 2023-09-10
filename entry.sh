#!/bin/sh

cd /app

python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input --clear
gunicorn HeyerAppDjango.wsgi:application --bind 0.0.0.0:8000