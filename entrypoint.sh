#!/bin/bash



# Apply database migrations
echo "Apply database migrations"
cd django_test
python manage.py makemigrations
python manage.py migrate

