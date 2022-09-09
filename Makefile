start:
	docker-compose up --build

lint:
	docker-compose run web flake8 .

format:
	docker-compose run web black .

build:
	docker-compose build
