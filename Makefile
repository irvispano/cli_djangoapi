install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --cov django_test django_test

format:
	black django_test

lint:
	flake8 --ignore=E501,W503,E125 django_test 
build:
	docker-compose up -d

all: install lint test
