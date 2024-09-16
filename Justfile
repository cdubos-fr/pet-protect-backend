set shell := ["zsh", "-uc"]

devenv:
    tox devenv -e devenv .venv
    pre-commit install

serve-docs:
    mkdocs serve

clean:
    find . -type d -name .venv -exec rm -rf {} +
    find . -type d -name __pycache__ -exec rm -rf {} +
    find . -type d -name .ruff_cache -exec rm -rf {} +
    find . -type d -name dist -exec rm -rf {} +
    find . -type d -name build -exec rm -rf {} +
    find . -type d -name .pytest_cache -exec rm -rf {} +
    find . -type d -name "*.egg-info" -exec rm -rf {} +
    find . -type d -name .mypy_cache -exec rm -rf {} +
    find . -type d -name .direnv -exec rm -rf {} +
    find . -type d -name .tox -exec rm -rf {} +
    find . -type d -name site -exec rm -rf {} +
    find . -type f -name .coverage -exec rm -rf {} +
    find . -type d -name result -exec rm -rf {} +
    find . -type d -name __pycache__ -exec rm -rf {} +

lock:
    pdm lock -G :all

migrate:
    alembic revision --autogenerate

db_upgrade:
    alembic upgrade head

db_downgrade:
    alembic downgrade base

check:
    tox
