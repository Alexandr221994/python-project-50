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

lint:
	poetry run flake8 gendiff
