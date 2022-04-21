# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ARG APP_DIR=backend
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

# ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

# Run database
# docker run --name mypostgres --network star-burger --network-alias database -p 5431:5432 -e POSTGRES_USER=yulia -e POSTGRES_PASSWORD=gfkfnf6 -e POSTGRES_DB=star-burger -d postgres

# Run backend
# docker run -d --rm --name burger-django --network star-burger --network-alias back -p 8000:8000 -p 5431:5432 --env-file ../.env -v /home/yulia/docker/bundles:/backend/bundles:ro burger_back

# Run shell
# docker run --rm -ti --entrypoint /bin/bash --env-file ../.env burger_back
