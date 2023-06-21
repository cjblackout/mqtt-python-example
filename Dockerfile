# Use the official Python Alpine image as the base image
FROM python:3.9.17-alpine3.18

# Set the working directory inside the container
WORKDIR /app

# Copy the Python scripts and requirements.txt to the working directory
COPY sender.py receiver.py requirements.txt ./

# Install the required dependencies
RUN apk --no-cache add gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev libffi-dev openssl-dev

# Run both the MQTT sender and receiver
CMD [ "sh", "-c", "python sender.py & python receiver.py" ]