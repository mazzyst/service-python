prepare:
	pipenv install Flask
	pipenv install pytest


test:
	pipenv run pytest

.PHONY: all test clean

run:
	pipenv run python *.py


