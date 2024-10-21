#!/bin/bash

# read secrets from environment variables
export POSTGRES_USER=$(cat /run/secrets/postgres_user)
export POSTGRES_PASSWORD=$(cat /run/secrets/postgres_password)
export POSTGRES_DB=$(cat /run/secrets/postgres_db)

# Start PostgreSQL with environment variables
exec docker-entrypoint.sh postgres
