#!/bin/bash
# start_server.sh
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Check if database has already been seeded
if [ ! -f /app/db_seeded ]; then
  echo "Seeding Database"
  python manage.py seed_db
  touch /app/db_seeded
else
  echo "Database already seeded"
fi

# Run tests
echo "Running tests"
pytest

# Start server
echo "Starting server"
# python manage.py runserver 0.0.0.0:8000
gunicorn genes_test.wsgi:application --bind 0.0.0.0:8000