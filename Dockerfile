# Use a small Python base image
FROM python:3.11-slim

# PYTHONUNBUFFERED prints log imm without buffering, PYTHONDONTWRITEBYTECODE dont write .pyc
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Workdir inside the container
WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# FastAPI default port
EXPOSE 8000

# Start the app (your app is app/main.py → app.main:app)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
