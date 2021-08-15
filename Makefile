ifndef $(version)
  version = development
endif

run-local:
	gunicorn --reload -w 1 src.api.main:app

.PHONY: tests
tests:
	pytest tests

build:
	docker build -t rest_api_sample:$(version) .

run:
	docker run -p 8000:8000 rest_api_sample:$(version)