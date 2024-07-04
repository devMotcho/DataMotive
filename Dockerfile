# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .


RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# Command to run the application
CMD ["python", "app.py"]