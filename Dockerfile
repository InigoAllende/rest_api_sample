
FROM python:3.9-slim-buster

RUN apt-get update 
RUN pip install poetry

COPY poetry.lock pyproject.toml /app/
COPY ./src /app/src

WORKDIR /app

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

CMD gunicorn -w 1 -b 0.0.0.0:8000 src.api.main:app