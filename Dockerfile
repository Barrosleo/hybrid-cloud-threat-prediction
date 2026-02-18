# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency files first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/ ./src/
COPY models/ ./models/
COPY deployment/sample_request.json ./sample_request.json

# Expose API port
EXPOSE 8000

# Set environment variables (optional but recommended)
ENV PYTHONUNBUFFERED=1
ENV MODEL_PATH=models/random_forest.pkl

# Start the FastAPI inference server using uvicorn
CMD ["uvicorn", "src.score:app", "--host", "0.0.0.0", "--port", "8000"]
