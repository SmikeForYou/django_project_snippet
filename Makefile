MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MKFILE_DIR := $(dir $(MKFILE_PATH))
PROJECT_NAME=project_name
DJANGO_APP_ROOT=${MKFILE_DIR}${PROJECT_NAME}

# Common
local:
	@docker-compose -f docker-compose.local.yml up --build $(PROJECT_NAME)_app

_local:
	python3 $(DJANGO_APP_ROOT)/manage.py runserver 0.0.0.0:8080

dev:
	@docker-compose -f docker-compose.dev.yml up -d --build

_gunicorn: 
	gunicorn --chdir ${DJANGO_APP_ROOT} ${PROJECT_NAME}.wsgi:application -b 0.0.0.0:8080

_uvicorn:
	PYTHONPATH=${DJANGO_APP_ROOT} python ${DJANGO_APP_ROOT}/${PROJECT_NAME}/asgi.py

_dev: wait_resources _migrate _collectstatic _initadmin _uvicorn

bash:
	@docker exec -it $(PROJECT_NAME) bash

wait_resources:
	PYTHONPATH=${DJANGO_APP_ROOT} python3 $(DJANGO_APP_ROOT)/utils/wait_script.py

# Django Services Wrapper
_migrations:
	python3 $(PROJECT_NAME)/manage.py makemigrations --noinput

migrations:
	@docker exec -it $(PROJECT_NAME) make _migrations

_migrate:
	python3 $(PROJECT_NAME)/manage.py migrate --noinput

migrate:
	@docker exec -it $(PROJECT_NAME) make _migrate

_collectstatic:
	python3 $(PROJECT_NAME)/manage.py collectstatic --no-input --clear

collectstatic:
	@docker exec -it $(PROJECT_NAME) make _collectstatic

_initadmin: 
	python3 $(PROJECT_NAME)/manage.py initadmin

initadmin:
	@docker exec -it $(PROJECT_NAME) make _initadmin


# Linters & Formaters
	# TODO: ...