# DataMotive

---

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

DataMotive is meant to be an open-source Inventory Management System which provides users a simple way to track their products stock and business flow in a user-friendly way developed with Python/Django for backend, html + bootstrap + Vanilla JavaScript for the frontend and PostgreSQL for the database dockerized so it can run on any machine.

### Features

---

### Tech Stack

---

- **Backend** : Django
- **Frontend**: HTML, Bootstrap, CSS, Vanilla JavaScript
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
