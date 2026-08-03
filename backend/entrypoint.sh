#!/usr/bin/env bash
set -e

# simple wait-for-postgres
host="${POSTGRES_HOST:-postgres}"
port="${POSTGRES_PORT:-5432}"
user="${POSTGRES_USER:-fftf_admin}"

export PGPASSWORD="${POSTGRES_PASSWORD:-fftf_password}"

echo "Waiting for postgres at ${host}:${port}..."

until pg_isready -h "$host" -p "$port" -U "$user" >/dev/null 2>&1; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up - executing command"

exec "$@"
