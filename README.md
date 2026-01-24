# Task API

## Project Overview
This project demonstrates a production-style DevOps workflow for a simple Flask-based service. The focus is on delivery, deployment, and observability. The system is containerized, automatically built and deployed via CI/CD, runs on AWS, and exposes metrics and logs for monitoring.
The application acts as a small internal service used to validate DevOps practices such as health checks, monitoring, alerting, and automated deployments.

## Project Goals
- Build a simple, predictable API to generate traffic, logs, and metrics
- Containerize the application using Docker
- Implement CI/CD using GitHub Actions
- Deploy the service to AWS EC2
- Monitor application and system health using Prometheus and Grafana
- Expose structured logs suitable for production environments

## Application Purposes
The Flask application is intentionally minimal. Its purpose is to:
- Provide health and readiness signals
- Support basic CRUD-style interactions
- Emit logs and metrics for observability
- Simulate failures for monitoring and alert testing

## API Endpoints
```GET /health ``` — Service health check<br>
```POST /tasks ``` — Create a task<br>
```GET /tasks ``` — List all tasks<br>
```GET /fail ``` — Simulate application failure (intentional errors)<br>
```GET /metrics ``` — Prometheus metrics endpoint<br>

## Observability
### Logging
- Structured logs written to stdout
- Logs include request details, response status, and errors
- Startup and shutdown events are logged

### Metrics
- HTTP request count
- Request latency
- Error rate
- Custom application metrics (e.g., tasks created)
Metrics are scraped by Prometheus and visualized in Grafana dashboards.

## CI/CD Pipeline
The GitHub Actions pipeline performs the following steps:
1. Run automated tests
2. Build a Docker image
3. Push the image to a container registry
4. Deploy the updated image to AWS EC2

## Deployment
- Application runs inside a Docker container on AWS EC2
- Security groups restrict inbound traffic
- The service is accessible via the EC2 public IP

## Tech Stack
- Language: Python 3
- Framework: Flask
- Containerization: Docker
- CI/CD: GitHub Actions
- Cloud: AWS EC2
- Monitoring: Prometheus, Grafana
- Testing: pytest

## Status
In progress
