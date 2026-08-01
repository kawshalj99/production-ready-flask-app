# Production Ready Flask DevOps Project

![Python](https://img.shields.io/badge/Python-3.13-blue)

![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

![Flask](https://img.shields.io/badge/Flask-Web%20API-green)

![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-success)

![License](https://img.shields.io/badge/License-MIT-yellow)

A DevOps project demonstrating a complete CI pipeline using Docker, Docker Compose, GitHub Actions, Pytest, and Docker Hub.

-------------------------------------------------------------------

# Project Overview

This project was built to learn and demonstrate fundamental DevOps practices by containerizing a Flask application, automating testing, and implementing Continuous Integration using GitHub Actions.

-------------------------------------------------------------------

# Architecture

                GitHub

                   │
                   ▼

           GitHub Actions CI

          ┌────────────────┐
          │  Run Pytest    │
          │ Build Docker   │
          │ Push Image     │
          └────────────────┘

                   │
                   ▼

              Docker Hub

                   │
                   ▼

             Docker Compose

            ┌───────────────┐
            │ Flask API     │
            └──────┬────────┘
                   │
                   ▼
            ┌───────────────┐
            │ MySQL         │
            └───────────────┘

-------------------------------------------------------------------

# Features

- REST API built with Flask
- Dockerized application
- Multi-container deployment using Docker Compose
- MySQL integration
- Environment variable configuration
- Automated testing using Pytest
- Continuous Integration with GitHub Actions
- Automatic Docker image publishing to Docker Hub

-------------------------------------------------------------------

# Tech Stack

- Python 3.13
- Flask
- Docker
- Docker Compose
- MySQL
- Pytest
- GitHub Actions
- Docker Hub
- Git

-------------------------------------------------------------------

# Running the Project

Clone the repository

--Bash--
git clone https://github.com/kawshalj99/production-ready-flask-app.git

Build the Docker image

--Bash--
docker build -t production-ready-flask-app .

Run using Docker Compose

--Bash--
docker compose up -d

Open

http://localhost:5000


# Running Tests

--Bash--
python -m pytest -v

-------------------------------------------------------------------

# CI Pipeline

Every push to the **main** branch automatically:

- Checks out the repository
- Installs dependencies
- Runs automated tests
- Builds Docker image
- Pushes image to Docker Hub


Ashendra Kawshal

Github : https://github.com/kawshalj99

LinkedIn : www.linkedin.com/in/ashendrajayaneththige