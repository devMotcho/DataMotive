# DataMotive

## **\*** Under Development **\***

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

DataMotive is meant to be a Management System which provides a simple way to track products, stock and transactions flow in a user-friendly.

### Features

---

- Possibility to send custom bootstrap alerts with django.contrib.messages;
- CRUD Products;
- View Stock with Chart Js;
- Whenever a Product is Created a Django signal is sent to create a new instance of that Product in Stock with quantity 0;
- CRUD Categories, Measurements;
- CRUD Partners ( Suppliers and Clients) and their Entity Types;
- CRUD Transactions ( Sales and Purchases );
- Every Creation, Modification or Deletion of a Sales and Purchases is logically set so the Stock quantity and price are updated accordingly;
- Whenever a new User is Created a Django signal is sent to create a new instance of Profile with that User;
- Need to be Authenticated in order to View any content or data, if not you will be redirected to login page;
- Docker-compose will make migrations, migrate and create a super user for you;
- Use `pint` library to check the measurement;
- Pagination, django.core.paginations with bootstrap;
- Footer with search bar and socials;
- KPI's on the dashboard;

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

### License

DataMotive is distributed under MIT license.
