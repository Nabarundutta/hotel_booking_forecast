📊 Hotel Booking Forecast – MLOps End-to-End Project
This project demonstrates a complete MLOps pipeline for a Machine Learning model using MLflow, Docker, Jenkins, Google Cloud Platform, and GitHub. The pipeline includes data ingestion, model training, tracking, versioning, containerization, CI/CD, and cloud deployment with a focus on modular and maintainable code.

🚀 Project Overview
Problem Statement: Predict hotel booking cancellations using historical booking data.

Goal: Build, track, version, and deploy an ML model in production using MLOps best practices.

🧰 Tech Stack
Component	Tool/Service
Code Versioning	Git + GitHub
Model Tracking	MLflow
CI/CD	Jenkins
Cloud Storage	Google Cloud Storage (GCS)
Deployment	Google Cloud Run
Containerization	Docker
Orchestration	Jenkinsfile
Language	Python
Structure	Modular Python Packages

📁 Project Structure
bash
Copy
Edit
hotel_booking_forecast/
│
├── data/                      # Data ingestion scripts
├── models/                    # Model training and MLflow logging
├── pipelines/                 # Preprocessing and pipeline steps
├── utils/                     # Helper functions
├── Dockerfile                 # Docker container specification
├── Jenkinsfile                # CI/CD pipeline
├── requirements.txt           # Python dependencies
├── app/                       # API/app (optional for prediction endpoint)
├── mlruns/                    # MLflow tracking artifacts
└── main.py                    # Entry point
🔄 Workflow
✅ 1. Data Ingestion
Data is fetched directly from Google Cloud Storage (GCS) buckets.

Modularized ingestion code in data/.

📊 2. Preprocessing & Feature Engineering
Feature pipelines built using Scikit-learn Pipelines.

Encapsulated in pipelines/.

🔁 3. Model Training
Models trained and evaluated using modular scripts.

MLflow used for:

Tracking experiments

Logging parameters, metrics, and artifacts

Registering models

🔖 4. Version Control
All code is tracked in GitHub.

MLflow tracks model versions alongside code versions (commit hash tagging).

🐳 5. Dockerization
Dockerfile includes all dependencies and scripts.

Built for portability and reproducibility.

🛠️ 6. CI/CD with Jenkins
Jenkins pipeline (Jenkinsfile) automates:

Cloning repo

Running unit tests

Building Docker image

Pushing to Container Registry

Deploying to Google Cloud Run

☁️ 7. Deployment on Google Cloud Run
Lightweight API or model server deployed as a serverless container.

Scales automatically based on incoming traffic.

📦 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/<your-username>/hotel_booking_forecast.git
cd hotel_booking_forecast
2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Mac/Linux
# .\venv\Scripts\activate  # On Windows
pip install -r requirements.txt
3. Configure GCP Access
Authenticate using gcloud auth login.

Set up service account credentials and export:

bash
Copy
Edit
export GOOGLE_APPLICATION_CREDENTIALS="path_to_service_account.json"
4. Run MLflow Locally
bash
Copy
Edit
mlflow ui
5. Docker Build & Run (for testing)
bash
Copy
Edit
docker build -t hotel-forecast-app .
docker run -p 5000:5000 hotel-forecast-app
🔁 CI/CD with Jenkins
The Jenkins pipeline automates:

Pulling from GitHub

Running unit tests

Building Docker image

Pushing to Google Container Registry

Deploying to Google Cloud Run

Sample Jenkinsfile snippet:

groovy
Copy
Edit
pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t gcr.io/$PROJECT_ID/hotel-forecast .'
            }
        }
        stage('Push to GCR') {
            steps {
                sh 'docker push gcr.io/$PROJECT_ID/hotel-forecast'
            }
        }
        stage('Deploy to Cloud Run') {
            steps {
                sh 'gcloud run deploy hotel-forecast --image gcr.io/$PROJECT_ID/hotel-forecast --region asia-south1'
            }
        }
    }
}
🧪 MLflow Tracking Example
Each training run is logged with:

Parameters: Model type, hyperparameters

Metrics: Accuracy, F1-score, etc.

Artifacts: Model pickle files, confusion matrices

Source: Git commit hash for reproducibility

📌 Key Features
✅ End-to-End automation

✅ Reproducible ML experiments

✅ Scalable cloud deployment

✅ Modular and clean codebase

✅ Docker + Jenkins + MLflow integration

📬 Contact
Made with ❤️ by Nabarun Dutta
For queries, reach me at: [your-email@example.com]