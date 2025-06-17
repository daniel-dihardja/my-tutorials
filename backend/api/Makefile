COMPOSE_FILE=docker-compose.dev.yml
ENV_FILE=../.env

start-db:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up -d db

stop-db:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) stop db

clean-db:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) down -v

logs-db:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) logs -f db

status:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) ps

# Starts DB and runs Django dev server (sync)
runserver: start-db
	poetry run env PYTHONPATH=src python manage.py runserver

# Starts DB and runs ASGI GraphQL/Django server with uvicorn (async)
start: start-db
	poetry run env PYTHONPATH=src uvicorn config.asgi:application --reload --host 0.0.0.0 --port 8000
