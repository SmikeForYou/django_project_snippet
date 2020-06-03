MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MKFILE_DIR := $(dir $(MKFILE_PATH))
PROJECT_NAME=project_name
DJANGO_APP_ROOT=${MKFILE_DIR}
MANAGE_FILE=${DJANGO_APP_ROOT}/manage.py
# Common

_local:
	python3 $(DJANGO_APP_ROOT)/manage.py runserver 0.0.0.0:8080

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
	python3 ${MANAGE_FILE} makemigrations --noinput

migrations:
	@docker exec -it $(PROJECT_NAME) python3 ${MANAGE_FILE} makemigrations --noinput

_migrate:
	python3 ${MANAGE_FILE} migrate --noinput

migrate:
	@docker exec -it $(PROJECT_NAME) python3 ${MANAGE_FILE} migrate --noinput

_collectstatic:
	python3 ${MANAGE_FILE} collectstatic --no-input --clear

collectstatic:
	@docker exec -it $(PROJECT_NAME) python3 ${MANAGE_FILE} collectstatic --no-input --clear

_initadmin: 
	python3 ${MANAGE_FILE} initadmin

initadmin:
	@docker exec -it $(PROJECT_NAME) python3 ${MANAGE_FILE} initadmin


# Linters & Formaters
	# TODO: ...
	