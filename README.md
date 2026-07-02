# Dockerized REST API with CI

A simple REST API built with Flask, containerized using Docker, and tested automatically via a GitHub Actions CI pipeline on every push.

## Features

- RESTful endpoints for managing a list of tasks
- Containerized with Docker for consistent environments
- Automated tests with pytest
- GitHub Actions workflow that runs tests and builds the Docker image on every push

## Tech Stack

- Python / Flask
- Docker
- GitHub Actions

## Getting Started

### Run Locally (without Docker)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the server:
   ```bash
   python app.py
   ```

3. Visit `http://localhost:5000`

### Run with Docker

1. Build the image:
   ```bash
   docker build -t flask-tasks-api .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 flask-tasks-api
   ```

3. Visit `http://localhost:5000`

## API Endpoints

| Method | Endpoint        | Description          |
|--------|-----------------|----------------------|
| GET    | /tasks          | List all tasks       |
| GET    | /tasks/<id>     | Get a task by ID     |
| POST   | /tasks          | Create a new task    |
| DELETE | /tasks/<id>     | Delete a task        |

### Example Requests

**Create a task:**
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries"}'
```

**Get all tasks:**
```bash
curl http://localhost:5000/tasks
```

## Running Tests

```bash
pytest test_app.py
```

## CI/CD

Every push to the repository triggers a GitHub Actions workflow that:
1. Installs dependencies
2. Runs the test suite with pytest
3. Builds the Docker image to verify it compiles successfully