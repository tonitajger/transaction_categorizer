.PHONY: install format lint lint_fix
install:
	poetry install

format:
	poetry run ruff format transaction_categorizer notebooks
	poetry run ruff --select I --fix transaction_categorizer notebooks

lint:
	poetry run ruff transaction_categorizer notebooks

lint_fix:
	poetry run ruff transaction_categorizer notebooks --fix
