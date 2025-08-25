
# ---- Runtime image ----
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1

WORKDIR /app

# Install deps
COPY requirements.txt .
RUN python -m pip install --upgrade "setuptools>=78.1.1,<79.0.0"
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY app ./app
COPY .env.example ./.env

# Expose & run
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
