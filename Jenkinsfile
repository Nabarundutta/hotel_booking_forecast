pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = 'decisive-circle-462313-s7'
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        IMAGE_NAME = "ml-project"
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Clone GitHub Repository') {
            steps {
                script {
                    echo 'Cloning GitHub repository...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/Nabarundutta/hotel_booking_forecast.git'
                        ]]
                    )
                }
            }
        }

        stage('Setup Virtual Environment (Optional)') {
            steps {
                script {
                    echo 'Creating virtual environment and installing dependencies...'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Build and Push Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Building and pushing Docker image...'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/${IMAGE_NAME}:${IMAGE_TAG} .
                        docker push gcr.io/${GCP_PROJECT}/${IMAGE_NAME}:${IMAGE_TAG}
                        '''
                    }
                }
            }
        }

        stage('Run Training Pipeline Inside Container') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Running training pipeline inside Docker container...'
                        sh '''
                        docker run --rm \
                          -v ${GOOGLE_APPLICATION_CREDENTIALS}:${GOOGLE_APPLICATION_CREDENTIALS} \
                          -e GOOGLE_APPLICATION_CREDENTIALS=${GOOGLE_APPLICATION_CREDENTIALS} \
                          gcr.io/${GCP_PROJECT}/${IMAGE_NAME}:${IMAGE_TAG} \
                          python pipeline/training_pipeline.py
                        '''
                    }
                }
            }
        }
    }
}
