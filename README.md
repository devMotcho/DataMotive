# DataMotive


### Table of Contents

---

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Config](#conf)
- [Docker](#docker)
- [License](#license)

### Introduction

---

DataMotive is meant to be a Management System which provides a simple way to track products, stock and transactions flow in a user-friendly way, feel free to contribute with this project development in any way!

### Features

---

- Possibility to send custom bootstrap alerts with django.contrib.messages;
- Visualize Data with Chart Js;
- KPI's cards on the dashboard;
- Footer with search bar and socials;
- Pagination, django.core.paginations with bootstrap;
- CRUD Products;
- CRUD Categories, Measurements;
- CRUD Partners ( Suppliers and Clients) and their Entity Types;
- CRUD Transactions ( Sales and Purchases );
- Every Creation, Modification or Deletion of a Sales and Purchases is logically set so the Stock quantity and price are updated accordingly;
- Whenever a new Product is Created a Django signal is sent to create a new instance of that Product in Stock with quantity 0;
- Whenever a new User is Created a Django signal is sent to create a new instance of Profile with that User;
- Need to be Authenticated in order to View any content or data, if not you will be redirected to login page;
- Docker-compose will make migrations, migrate and create a super user;
- Use `pint` library to check the measurement;

### Tech Stack

---

- **Backend** : Django
- **Frontend**: HTML, Bootstrap, CSS, JavaScript
- **Database**: PostgreSQL
- **Containerization**: Docker

### Prerequisites

---

- Python (https://www.python.org/downloads/)
- Docker (https://www.docker.com/products/docker-desktop/)

### Installation

---

To get a local copy up and running follow these simple example steps.

1. **Clone the repository**:

```bash
git clone https://github.com/devMotcho/DataMotive.git
cd DataMotive
```

2. **Create a .env in the root of the project and edit it to set your environment variables**:

```.env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=datamotive
DATABASE_USER=your-db-user
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=db
DATABASE_PORT=5432
```

3. **Build and run the Docker containers**:

```bash
docker-compose up --build
```

4. **Apply the database migrations**:

```bash
docker-compose exec web python manage.py migrate
```

5. **Create a superuser**:

You have a default super user created:

- username : admin
- password : adminpassword

```bash
docker-compose exec web python manage.py createsuperuser
```

### Configuration

---

Set up environment variables in the .env file as mentioned above:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=datamotive
DATABASE_USER=your-db-user
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=db
DATABASE_PORT=5432
```

### Docker

---

To start the development server:

```bash
docker-compose up
```

To stop the development server:

```bash
docker-compose down
```

You can access the development server at **localhost:8000**


### S3 Bucket for Images
In production the images are being store on a s3 bucket, add this with the actual values of your s3 bucket to your .env file:

```
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_scret_access_key
AWS_STORAGE_BUCKET_NAME=your_aws_storage_bucket_name
```

### License

DataMotive is distributed under MIT license.
