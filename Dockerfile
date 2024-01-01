# Use the official Ubuntu base image
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Update the package repository and install any necessary packages
RUN apt-get update

RUN apt-get install -y nodejs && \
    apt-get install -y npm &&\
    apt-get install -y python3 &&\
    apt-get install -y python3-pip

COPY . .

CMD ["tail", "-f", "/dev/null"]
