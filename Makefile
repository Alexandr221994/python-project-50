install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --force-reinstall dist/*.whl

gendiff:
	poetry run gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests

lint:
	poetry run flake8 gendiff
