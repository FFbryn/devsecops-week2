pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build') {
      steps {
        echo 'Building project...'
      }
    }

    stage('Test') {
      steps {
        sh 'pytest'
      }
    }

    stage('Security Scan') {
      steps {
        sh 'bandit -r .'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying application to staging environment...'
      }
    }
  }

  post {
    success {
      echo 'Pipeline completed successfully!'
    }
    failure {
      echo 'Pipeline failed.'
    }
  }
}

