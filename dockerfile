# Use an official Python runtime as a parent image
FROM python:3.12.7-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any required packages
RUN apt-get update && \
    apt-get install -y python3-tk xvfb && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make the container's port available to the outside
EXPOSE 8000

# Run Xvfb and then start the application
CMD ["xvfb-run", "python", "main.py"]
