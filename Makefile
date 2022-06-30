.PHONY: install update format lint lint-darker migration test security export run

install:
	@poetry install
update:
	@poetry update	
format:
	@poetry run blue .
	@poetry run isort .
#Recommend for pre-commit hook if starting project
lint:
	@poetry run blue . --check
	@poetry run isort . --check
#Recommend for pre-commit hook if the project has already started
lint-darker:
	@poetry run darker . --check
	@poetry run darker .  --isort
migration:
	@poetry run alembic upgrade head
test:
	@poetry run pytest -v
security:
	@poetry run pip-audit
export:
	@poetry export -f requirements.txt --without-hashes  > requirements.txt
	@poetry export --dev -f  requirements.txt --without-hashes  > requirements-dev.txt
run:
	@poetry run uvicorn witsml_consumer_api.main:app --host localhost --port 8080 --reload --log-level debug
