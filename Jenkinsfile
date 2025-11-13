pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/FFbryn/devsecops-week2.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building application..."'
            }
        }

        stage('Test') {
            steps {
                sh '''
                pip install -r requirements.txt
                pip install pytest
                pytest
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                pip install bandit
                bandit -r src
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying application to staging environment..."'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
