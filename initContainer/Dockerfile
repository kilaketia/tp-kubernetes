# syntax=docker/dockerfile:1.4
FROM python:3.12-alpine AS builder

WORKDIR /app

COPY . /app
RUN mkdir -p /data/

ENTRYPOINT ["python3"]
CMD ["app.py"]
app.py Dockerfile