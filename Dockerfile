# syntax=docker/dockerfile:1.4
FROM python:3.12-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app
RUN mkdir -p /data/

ENTRYPOINT ["python3"]
CMD ["app.py"]
