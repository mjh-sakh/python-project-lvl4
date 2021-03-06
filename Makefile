#Makefile

install:
	poetry install

lint:
	poetry run flake8 task_manager

reps:
	poetry show --tree

test:
	#poetry run mypy task_manager
	poetry run coverage run -m pytest

coverage:
	poetry run coverage xml

covhtml:
	poetry run coverage run -m pytest
	rm -r htmlcov
	poetry run coverage html
	open htmlcov/index.html

run:
	python manage.py runserver

open:
	open http://127.0.0.1:8000/

export:
	poetry export -f requirements.txt -o requirements.txt

update-ru:
	django-admin makemessages -l ru

compile-all:
	django-admin compilemessages
	
init:
	python manage.py migrate
	python manage.py collectstatic
	python manage.py createsuperuser