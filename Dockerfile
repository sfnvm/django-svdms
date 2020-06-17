# pull official base image
FROM python:3.7.7-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /code
WORKDIR /code

# python3 issues with psycopg2-binary
# source1: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
# source2: https://stackoverflow.com/questions/46711990/error-pg-config-executable-not-found-when-installing-psycopg2-on-alpine-in-dock
# install psycopg2 dependencies
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# copy project
COPY . /code/