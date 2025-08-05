pipeline{
    agent any 

    environment{
        VENV_DIR = 'venv'

    }

    stages{
        stage('Cloning github repo to jenkins'){
            steps{
                script{
                    echo 'Cloning github repo to jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Nabarundutta/hotel_booking_forecast.git']])
                }
            }
        }

        stage('Setting up our virtual enviornment and installing dependencies'){
            steps{
                script{
                    echo 'Setting up our virtual enviornment and installing dependencies'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
}