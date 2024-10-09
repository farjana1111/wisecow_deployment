# Use an official Ubuntu base image
FROM ubuntu:20.04

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    cowsay \
    fortune-mod \
    netcat

# Copy the current directory (application code) to /app in the container
COPY . /app

# Expose the port that the Wisecow app runs on
EXPOSE 4499

# Start the application
CMD ["./wisecow.sh"]
