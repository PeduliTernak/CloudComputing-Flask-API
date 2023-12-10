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

Build the Docker image and run the Docker container, or [Deploy to Cloud Run](https://cloud.google.com/run/docs/deploying)

```bash
docker build -t model-deployment .
docker run -p 8080:8080 -d model-deployment
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
