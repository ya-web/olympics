# Django Backend with PostgreSQL - Docker Swarm

This project is a Django backend application orchestrated with Docker Swarm, using PostgreSQL as the database.

## Prerequisites

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Swarm** initialized: [Docker Swarm Init](https://docs.docker.com/reference/cli/docker/swarm/init/)

## Project Structure

- **Django**: Serves the backend of the application.
- **PostgreSQL**: Manages the relational database.
- **Docker Swarm**: Orchestrates the services.

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

Edit the `.env` file with appropriate values (check `.env.sample` file)

### 3. Build the Django image:

Before deploying with Docker Swarm, you need to build the **Django** image:

```bash
docker build -t your-dockerhub-username/django:latest .
```

### 4. Create Docker secrets for sensitive data:

```bash
  echo "your_secret_key" | docker secret create django_secret_key -
  echo "your_db_user" | docker secret create postgres_user -
  echo "your_db_password" | docker secret create postgres_password -
  echo "your_db_name" | docker secret create postgres_db -
```

### 5. Deploy the stack with Docker Swarm

```bash
docker stack deploy -c stack.yaml django-backend
```

### 6. Check the running services

```bash
docker service ls
```

### 7. Access the Django application at `http://localhost:8000`

## Now begin a new Django and PostgreSQL project manage with Docker Swarm
