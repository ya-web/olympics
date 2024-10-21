FROM python:3.10-slim-bullseye

# Add metadata for versioning and author information
LABEL maintainer="Idir Alliche <tixidest@gmx.com>"
LABEL version="1.0"
LABEL description="Django backend application"
LABEL github="https://github.com/ya-web"
LABEL dockerhub="https://hub.docker.com/u/tixidest"

# Disable Python's output buffering and prevent .pyc files generation
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

ARG USERNAME=django_user
ARG USER_UID=1001
ARG USER_GID=1001

# Create a user and group dynamiquement
RUN groupadd -g ${USER_GID} ${USERNAME} && \
    useradd -u ${USER_UID} -g ${USER_GID} -ms /bin/bash ${USERNAME}

# Set the environment variable for the Django project
# 'dev' or 'prod', 'stag', 'test'
ARG ENVIRONMENT=dev
ENV ENVIRONMENT=${ENVIRONMENT}

# Install minimal system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /backend
# Ensure the non-root user owns the /backend directory
RUN chown -R ${USERNAME}:${USERNAME} /backend

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

# Switch to the non-root user
USER ${USERNAME}

# Run Gunicorn to serve the Django app
CMD ["gunicorn", "django_backend.wsgi:application", "--bind", "0.0.0.0:8000", "--reload"]

EXPOSE 8000