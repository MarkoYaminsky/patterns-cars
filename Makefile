runserver:
	make migrate
	python manage.py runserver

install-requirements:
	pip install -r requirements.txt

launch-docker:
	docker compose up -d
	make runserver

launch-docker-build:
	docker compose up --build -d
	make read

migrate:
	python manage.py migrate