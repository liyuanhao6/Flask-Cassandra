#!/usr/bin/sh
# Construct a network
docker network create my-net --driver bridge

# Cassandra server
# Pull cassandra image from Docker Hub
docker pull cassandra:latest
# Run the cassandra container
docker run -d --name my-cassandra \
-v ~/docker/data/cassandra:/app/data \
-p 9042:9042 \
--network my-net \
cassandra:latest

# Flask server
# Build flask image
docker build -t flask-app .
# Run the flask server
docker run -d --name my-flask \
-v ~/docker/data/flask:/app/data \
-p 8080:8080 \
--network my-net \
flask-app

# Common commands:
POST
curl -X POST -F 'image=@<image_path>' -v http://0.0.0.0:8080/api/tasks/upload
GET ALL
curl -X GET http://0.0.0.0:8080/api/tasks
GET
curl -X GET http://0.0.0.0:8080/api/tasks/<int:task_id>

