.PHONY: format lint typecheck test check

format:
	uv run ruff format

lint:
	uv run ruff check

typecheck:
	uv run ty check

test:
	uv run python -m pytest tests

check: format lint typecheck test