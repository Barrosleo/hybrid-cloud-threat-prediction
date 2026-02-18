# Docker Usage Guide
This guide explains how to build, run, and test the containerized version of the Hybrid Cloud Threat Prediction API.

The Docker image contains:
- The trained machine learning model
- The FastAPI inference server
- All required dependencies
- A REST API endpoint for predictions

---

## 1. Prerequisites

Before you begin, ensure you have:

- **Docker Desktop** installed and running  
  Download: https://www.docker.com/products/docker-desktop/

- The repository cloned locally:
```bash
git clone https://github.com/<your-username>/hybrid-cloud-threat-prediction.git
cd hybrid-cloud-threat-prediction
```

## 2. Build the Docker Image
Run the following command from the root of the repository (where the Dockerfile is located):

```bash
docker build -t hybrid-threat-api .
```

This command:

Reads the Dockerfile

Installs dependencies

Copies your model + source code

Creates a runnable image named hybrid-threat-api

## 3. Run the Container
Start the API server:

```bash
docker run -p 8000:8000 hybrid-threat-api
```

This exposes the API at:

Code
```
http://localhost:8000
```
You should see output similar to:

Code
```
Uvicorn running on http://0.0.0.0:8000
```

## 4. Test the API
Open a second terminal window and run:

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d @deployment/sample_request.json
```

Expected response:
```
json
{
  "prediction": 0,
  "label": "Normal"
}
```
or
```
json
{
  "prediction": 1,
  "label": "Attack"
}
```
## 5. Interactive API Documentation
FastAPI automatically generates interactive docs.

Open your browser and visit:

Code
```
http://localhost:8000/docs
```
From here, you can:

Explore the API

Send prediction requests

Inspect input/output formats

## 6. Stopping the Container
Press:

Code
```
CTRL + C
```
Or list running containers:

```bash
docker ps
```

Then stop it:

```bash
docker stop <container-id>
```
