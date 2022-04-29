# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ARG APP_DIR=backend
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./app

EXPOSE 8000
