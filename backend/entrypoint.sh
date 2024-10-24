#!/bin/bash

# Read secrets from environment variables
export POSTGRES_USER=$(cat /run/secrets/postgres_user)
export POSTGRES_PASSWORD=$(cat /run/secrets/postgres_password)
export POSTGRES_DB=$(cat /run/secrets/postgres_db)

# Check if the service is Django (optional)
if [ "$SERVICE" = "django" ]; then
    # Collect static files
    echo "Collecting static files..."
    python manage.py collectstatic --noinput

    # Apply database migrations (optional)
    echo "Applying database migrations..."
    python manage.py migrate
fi

# Start the main process (PostgreSQL or Django server depending on the service)
exec docker-entrypoint.sh postgres

