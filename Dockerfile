# Use official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /ECOM

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Move into the folder where main.py is located
WORKDIR /ECOM/app

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]










