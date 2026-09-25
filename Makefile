.PHONY: install dev test lint build up down
install:
	python -m pip install -r requirements.txt
dev:
	flask --app app run --debug --host 0.0.0.0
test:
	pytest -q
lint:
	python -m compileall app.py
build:
	docker build -t launchpad:local .
up:
	docker compose up --build
down:
	docker compose down