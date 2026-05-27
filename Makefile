.PHONY: install lint format test check clean

install:
	pip install -r requirements-dev.txt
	pre-commit install

lint:
	ruff check .

format:
	ruff format .

test:
	pytest tests/ -v

check: lint test

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
