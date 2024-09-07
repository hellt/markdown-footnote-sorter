FROM python:3.12-alpine

WORKDIR /app

COPY fnsort.py /app

WORKDIR /work

ENTRYPOINT ["python", "/app/fnsort.py"]