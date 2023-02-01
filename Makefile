.PHONY: all
all: format lint cov

.PHONY: format
format:
	black --exclude '/\.venv/' .
	isort --profile black .

.PHONY: lint
lint:
	flake8 --exclude=.venv/ --ignore=E203,E501,W503
	isort --check-only --profile black .
	black --check --exclude '/\.venv/' .

.PHONY: test
test:
	python -Wall manage.py test

.PHONY: cov
cov:
	coverage run --source='.' --omit '.venv/*' manage.py test
	coverage report -m

pginit:
	PGDATA=postgres-data/ pg_ctl init

pgstart:
	PGDATA=postgres-data/ pg_ctl start

pgstop:
	PGDATA=postgres-data/ pg_ctl stop

reload:
	uwsgi --reload mataroa.pid

.PHONY: pipupgrade
pipupgrade:
	pip-compile -U --resolver=backtracking