# Use official Python base image
FROM python:3.9-slim-buster

# Install Flask
RUN pip install flask

# Set working directory in the container
WORKDIR /app

# Copy app.py to the container
COPY app.py .

# Expose port 5000
EXPOSE 5000

# Run the Flask app
ENTRYPOINT ["python", "app.py"]
