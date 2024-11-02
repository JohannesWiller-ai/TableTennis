##############################################################
# Stage 1: Build the Python executable
##############################################################
FROM python:3.10-slim as builder

# Set the working directory
WORKDIR /usr/src/app

# Install system packages required for Tkinter
RUN apt-get update && \
    apt-get install -y \
    python3-tk \
    tk-dev \
    tcl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install virtualenv
RUN pip install virtualenv

# Create a virtual environment
RUN virtualenv venv

# Activate the virtual environment
ENV VIRTUAL_ENV=/usr/src/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the current directory contents into the container
COPY . .

# Install PyInstaller to create the executable
RUN pip install pyinstaller

# Create the Python executable
RUN pyinstaller --onefile main.py --hidden-import=tkinter

##############################################################
# Stage 2 : Create the final image with only the executible
##############################################################

#TODO it is possible to create even slimmer image using debian:buster-slim or google's distroless images
FROM python:3.10-slim 

# Set the working directory
WORKDIR /usr/src/app

# Install system packages required for Tkinter
RUN apt-get update && \
    apt-get install -y python3-tk tk-dev tcl-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the executable from the builder stage
COPY --from=builder /usr/src/app/dist/main /usr/src/app/main

# Start the program
CMD ["/usr/src/app/main"]

# https://askubuntu.com/questions/1161646/is-it-possible-to-run-docker-container-and-show-its-graphical-application-window
