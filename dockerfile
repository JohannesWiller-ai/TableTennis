# Use an official Python runtime as a parent image
FROM python:3.12.7-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Tkinter (for GUI) for Debian-based distributions
RUN apt-get update && apt-get install -y python3-tk

# Make the container's port available to the outside
EXPOSE 8000

# Run main.py when the container launches
CMD ["python", "main.py"]
