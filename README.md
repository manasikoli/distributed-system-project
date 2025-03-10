# distributed-system-project
User Details Web Service

# Overview

This project is a full-stack web service that collects user details through a frontend form, processes them via a Flask backend, and stores them in a MySQL database. The application is containerized using Docker and deployed using Kubernetes.

# Technologies Used

Frontend: HTML, CSS, Nginx

Backend: Python (Flask), Flask-SQLAlchemy

Database: MySQL

Containerization: Docker, Docker Compose

Orchestration: Kubernetes

Version Control: GitHub

# Project Structure
|-- frontend/
|   |-- index.html
|   |-- Dockerfile
|
|-- backend/
|   |-- app.py
|   |-- requirements.txt
|   |-- Dockerfile
|
|-- k8s/
|   |-- frontend-deployment.yml
|   |-- backend-deployment.yml
|   |-- mysql-deployment.yml
|
|-- docker-compose.yml
|-- README.md

# Installation & Setup

1. Clone the Repository
git clone <your-github-repo-url>
cd <your-repo-name>

2. Build and Run with Docker Compose
docker-compose up --build

3. Access the Application

Open http://localhost in your browser to view the frontend.

The backend API runs at http://localhost:5000/api/user.

4. Push Docker Images to Docker Hub
docker build -t <your-dockerhub-username>/frontend ./frontend

docker build -t <your-dockerhub-username>/backend ./backend

docker push <your-dockerhub-username>/frontend

docker push <your-dockerhub-username>/backend

# Deploying on Kubernetes

1. Apply Kubernetes Deployments
kubectl apply -f k8s/frontend-deployment.yml
kubectl apply -f k8s/backend-deployment.yml
kubectl apply -f k8s/mysql-deployment.yml

2. Expose Frontend Service
kubectl expose deployment frontend --type=LoadBalancer --port=80

# API Endpoints

POST /api/user

Description: Stores user details in the database.

# Request Body:
{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 25
}

# Response:
{
    "message": "User added successfully"
}
