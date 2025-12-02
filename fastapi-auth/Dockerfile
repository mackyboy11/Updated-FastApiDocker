# Use official Python runtime as a base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file and app files
COPY requirements.txt main.py auth.py crud.py database.py models.py setup_db.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create data directory for SQLite database
RUN mkdir -p /app/data

# Create a volume for the SQLite database
VOLUME ["/app/data"]

# Expose port 8000
EXPOSE 8000

# Initialize the database and run the application
CMD ["sh", "-c", "python setup_db.py && uvicorn main:app --host 0.0.0.0 --port 8000"]