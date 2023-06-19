#/bin/bash
# make script to run migrations from a container called 'web'
# Usage: ./run_migrations.sh
docker-compose run web python manage.py makemigrations --noinput
docker-compose run web python manage.py migrate --noinput