# Django Docker Project

This project containerizes a Django application using Docker, with dynamic user and environment management.

## Prerequisites

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Setup and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/ya-web/olympics
cd olympics
```

### 2. Create and Configure the `.env` File

Create a `.env` file from the provided `.env.sample`:

```bash
cp .env.sample .env
```

Edit the `.env` file with appropriate values:

```bash
USERNAME=django_user
USER_UID=1001
USER_GID=1001
ENVIRONMENT=dev
```

### 3. Build and Run the Application

Build the Docker image and run the service using Docker Compose:

```bash
docker compose up --build
```

### 4. Access the Application

The Django app will be available at:

```
http://localhost:8000
```

## Managing Secrets

Secrets are managed using a `secrets.json` file, which is ignored in `.dockerignore` file:

### Place your secrets in `secrets.json`:

```json
{
  "SECRET_KEY": "your_secret_key",
  "DATABASE_URL": "postgres://user:password@localhost:5432/mydatabase"
}
```
