# Use an official Python runtime as a parent image
FROM python:3.9-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project code into the container
COPY . /app/

RUN chmod +x /app/wait-for-it.sh && chmod +x /app/start_server.sh

# Expose the Django development server port
EXPOSE 8000

# Start the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "genes_test.wsgi", "--bind", "0.0.0.0:8000"]