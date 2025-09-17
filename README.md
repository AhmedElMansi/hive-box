# HiveBox App

HiveBox is a lightweight **Flask-based API** packaged in Docker and integrated with GitHub Actions for Continuous Integration (CI).  

The app currently provides:  
- A `/version` endpoint to return the application version.  
- A `/temperature` endpoint to simulate temperature data.  

---

## Features

- **Flask API**
- **Dockerized** for consistent deployment.  
- **CI pipeline** using GitHub Actions.
---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/AhmedElMansi/hive-box.git
cd hive-box
```
### 2. Build the Docker image
```
docker build -t hivebox:0.0.2 .
```
### 3. Run the container
```
docker run -d -p 5000:5000 --name hivebox hivebox:0.0.2
```
### 4. Access the endpoint
   Check version:     
```
curl http://127.0.0.1:5000/version
```

## CI/CD Workflow

The project includes a GitHub Actions workflow (.github/workflows/ci.yml) that runs on every push and pull request to main.
It performs the following checks:

1. Lint Python code with flake8.
2. Lint Dockerfile with hadolint.
3. Build Docker image.
4. Run container and test /version endpoint.
