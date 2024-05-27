runserver:
	make migrate
	docker exec -it cars-backend python manage.py runserver

install-requirements:
	docker exec -it cars-backend pip install -r requirements.txt

launch-docker:
	bash docker-launch.sh

launch-docker-build:
	bash docker-launch.sh build

migrate:
	docker exec -it cars-backend python manage.py migrate

loaddata:
	docker exec -it cars-backend python manage.py loaddata rent/fixtures/cars.json

create-super-user:
	docker exec -it cars-backend python manage.py createsuperuser