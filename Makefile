run:
	gunicorn --reload -w 1 src.api.main:app

.PHONY: tests
tests:
	pytest tests