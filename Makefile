prepare:
	pipenv install Flask
	piepenv install pytest


test:
	pipenv run pytest

.PHONY: all test clean

run:
	pipenv run python *.py


