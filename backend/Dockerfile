FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install runtime dependencies via pip (PEP517 with poetry-core in pyproject)
COPY pyproject.toml .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir .

# Copy app
COPY . .

# Make entrypoint executable
RUN chmod +x ./entrypoint.sh || true

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
