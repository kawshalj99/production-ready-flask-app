# Base image
FROM python:3.13-slim


# Create application directory
WORKDIR /app


# Copy dependency file first
COPY requirements.txt .


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy application code
COPY app ./app
COPY app.py .


# Create non-root user
RUN useradd -m appuser


# Switch user
USER appuser


# Application port
EXPOSE 5000


# Start application
CMD ["python", "app.py"]