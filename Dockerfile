# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY pyproject.toml poetry.lock /code/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
RUN poetry run python manage.py migrate

COPY . /code/