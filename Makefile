linter:
	poetry run flake8 financialprogramm

start:
	poetry run flask --app financialprogramm/routing --debug run



