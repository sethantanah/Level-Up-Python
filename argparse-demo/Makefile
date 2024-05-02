.PHONY: install run test

install:
	@docker-compose run --rm app poetry install

run:
	@docker-compose up --build

test:
	@docker-compose run --rm app poetry run pytest

# Default goal
.DEFAULT_GOAL := run
