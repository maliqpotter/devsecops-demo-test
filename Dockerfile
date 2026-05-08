
# ---- Runtime image ----
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:${PATH}"

# Create a non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup -m appuser

WORKDIR /app

# Install deps as root
COPY requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade \
    "pip>=25.0" \
    "setuptools>=78.1.1,<79.0.0" \
    "wheel>=0.46.2" \
    "jaraco.context>=6.1.0" \
    && pip install --no-cache-dir -r requirements.txt

# Copy source and set ownership
COPY app ./app
COPY .env.example ./.env
RUN chown -R appuser:appgroup /app
USER appuser


# Expose & run
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

