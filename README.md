# PeduliTernak - Flask (ML Model Deployment)

This repository contains the deployment of a Machine Learning Image Recognition Model. Predictions can be performed using API request methods.

## How to Use

1. Create and activate the virtual environment

   ```python
   python3 -m venv env
   source env/bin/activate
   ```

1. Install the packages and start the application

   ```python
   pip install -r requirements.txt
   flask run
   ```

## Deployment

Build the Docker image and run the Docker container

```bash
docker build -t ml-deployment .
docker run -p 8080:8080 -d ml-deployment
```

or [Deploy to Cloud Run](https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run) by configuring the `cloudbuild.yaml` and [`.gcloudignore`](https://cloud.google.com/sdk/gcloud/reference/topic/gcloudignore), then submit it

```bash
gcloud builds submit --config=cloudbuild.yaml
```

## API Documentation

### Summary

Base URL ([Require Authentication](https://cloud.google.com/run/docs/authenticating/service-to-service#acquire-token)): <https://flask-api-image-74e64w7rga-et.a.run.app/>

| Route | HTTP Method | Description               |
| ----- | ----------- | ------------------------- |
| /     | GET         | Health check              |
| /     | POST        | Perform image recognition |

### Endpoints

#### **GET `/` - Health check**

##### Request

- **Method:** GET
- **Path:** `/`

##### Response

- **Status: 200 OK**
  ```json
  {
    "status": true,
    "message": "OK"
  }
  ```

#### **POST `/` - Perform image recognition**

##### Request

- **Method:** POST
- **Path:** `/`
- **Body:**

  - **Form-Data** with a **single file** field named `file`
    ```yaml
    "file": image.jpg
    ```

##### Response

- **Status: 200 OK**

  ```json
  {
    "status": true,
    "prediction": "result"
  }
  ```

- **Status: 400 Bad Request**

  ```json
  {
    "status": false,
    "error": "no file"
  }
  ```

- **Status: 500 Internal Server Error**
  ```json
  {
    "status": false,
    "error": "error message"
  }
  ```
