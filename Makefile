.PHONY: install update format lint test security export run

install:
	@poetry install
update:
	@poetry update	
format:
	@poetry run blue .
	@poetry run isort .
lint:
	@poetry run blue . --check
	@poetry run isort . --check
test:
	@poetry run pytest -v
security:
	@poetry run pip-audit
export:
	@poetry export -f requirements.txt --without-hashes  > requirements.txt
	@poetry export --dev -f  requirements.txt --without-hashes  > requirements-dev.txt
run:
	@poetry run uvicorn witsml_consumer_api.main:app --host localhost --port 8080 --reload --log-level debug
