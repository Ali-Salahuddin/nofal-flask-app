# Flask Redis Application

## Overview
This is a simple Python Flask web application that connects to Redis.
Each time the homepage is accessed, a counter is incremented and displayed.

You do NOT need to modify application code.
Your task is to containerize and run this application using Docker.

---

## Application Details

- Language: Python 3
- Framework: Flask
- Dependency: Redis
- Application Port: 5000

---

## Files Explained

- app.py  
  Main Flask application.
  Reads Redis host and port from environment variables.

- requirements.txt  
  Python dependencies.

- Dockerfile  
  Instructions to build the Docker image.

- docker-compose.yml  
  Defines multi-container setup (Flask + Redis).

---

## Environment Variables

The application expects:

- REDIS_HOST  
- REDIS_PORT  

These are injected using Docker or Docker Compose.

---

## Running with Docker (Single Container)

> Redis must be running separately.

```bash
docker build -t flask-redis-demo .
docker run -p 5000:5000 flask-redis-demo
