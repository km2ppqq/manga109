.PHONY: build
build:
	poetry build

.PHONY: format
format:
	poetry run black -v manga109

.PHONY: install
install:
	poetry install

.PHONY: lint
lint:
	poetry run flake8 manga109
