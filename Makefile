# You can set these variables from the command line.
PORT =
ENV = production

MANAGE := python $(shell pwd)/djangoapp/manage.py

export PYTHONPATH := $(shell pwd)/djangoapp:$(PYTHONPATH)

serve:
	waitress-serve --port=$(PORT) {{ project_name }}.wsgi.$(ENV):application

migrate:
	$(MANAGE) migrate --settings={{ project_name }}.settings.$(ENV)
