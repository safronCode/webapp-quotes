FROM python:3.11-slim AS base

ENV PYTHONUNBUFFERED=1

WORKDIR /webapp-qoutes

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend .

COPY frontend/index.html templates/.

EXPOSE 8000

CMD ["gunicorn", "webapp_quotes.wsgi:application", "--bind", "0.0.0.0:8000"]
