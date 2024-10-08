# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /code

# copy project into the container
COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && pip install --no-cache-dir -r requirements.txt

RUN chmod +x /code/entrypoint.sh


ENTRYPOINT ["/code/entrypoint.sh"]


# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]