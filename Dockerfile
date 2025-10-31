FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Fixed: Use shell form to allow $PORT variable expansion
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
