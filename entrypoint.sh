#!/bin/sh
cd code
python manage.py migrate
#mkdir "static"
#python manage.py collectstatic --noinput
DJANGO_SUPERUSER_PASSWORD=admin@#3 ./manage.py createsuperuser     --no-input     --username=dozolab     --email=my_user@domain.com
#gunicorn --bind=localhost:8010 --workers 3 project.wsgi
python manage.py grpcrunserver --dev
python manage.py runserver 0.0.0.0:8010