# DiabeticRetinopathyClassification
Algorithm and SPA to predict Diabetic Retinopathy using basic image processing algorithms and Transfer Learning

## Running the project
Download and install **[Docker](https://runnable.com/docker/install-docker-on-windows-10).**

### Running the Back End
    1. docker pull zoli094/retinopathy_classification_backend
    2. docker run --name retinopathy_backend_container -p 8081:8081 zoli094/retinopathy_classification_backend
The backend will run on **port 8081**, so make sure that this port is not used by other programs!

### Running the Front End
    1. docker pull zoli094/retinopathy_classification_frontend
    2. docker run --name retinopathy_frontend_container -p 8080:5000 zoli094/retinopathy_classification_frontend
The frontend will run on **localhost:8080**.
