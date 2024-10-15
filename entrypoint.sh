#!/bin/bash
set -e

# Run database migrations
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
from product.models import Measurement
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')

if not Measurement.objects.filter(measure="Unit").exists():
    Measurement.objects.create(measure="Unit")

EOF

# Check if we are in development or production mode and run the appropriate command
if [ "$USE_DEV_ENV" = "1" ]; then
    echo "Running development server..."
    exec python manage.py runserver 0.0.0.0:8000
else
    echo "Running production server..."
    exec gunicorn mysite.wsgi:application --bind 0.0.0.0:8000
fi