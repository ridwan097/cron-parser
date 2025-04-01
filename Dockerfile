FROM python:3.11-slim

WORKDIR /app

COPY cron_cli.py .

ENTRYPOINT ["python", "cron_cli.py"]
