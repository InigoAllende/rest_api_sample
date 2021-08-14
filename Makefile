run-local:
	gunicorn --reload -w 1 src.api.main:app

.PHONY: tests
tests:
	pytest tests

build:
	docker build -t rest_api_sample:v$(version) .

run:
	sudo docker run -d -p 8000:8000 rest_api_sample:v$(version)