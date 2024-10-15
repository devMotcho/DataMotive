# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /code

# copy project into the container
COPY . .

# Environment configurations
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Argument to define the environment (default to production)
ARG USE_DEV_ENV=0
ENV USE_DEV_ENV=${USE_DEV_ENV}

# install dependencies
COPY ./requirements.txt .

# Install necessary dependencies for PostgreSQL and Python
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && pip install --no-cache-dir -r requirements.txt

# Make entrypoint executable
RUN chmod +x /code/entrypoint.sh

# Use the entrypoint script
ENTRYPOINT ["/code/entrypoint.sh"]

# Conditional CMD for development or production
CMD ["sh", "-c", "if [ \"$USE_DEV_ENV\" = \"1\" ]; then python manage.py runserver 0.0.0.0:8000; else gunicorn mysite.wsgi:application --bind 0.0.0.0:8000; fi"]
