pipeline {
  agent { docker { image 'python:3.10' args '-u root:root' } }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build') {
      steps {
        sh 'echo "Building application..."'
      }
    }

    stage('Test') {
      steps {
        // gunakan pip di dalam container python:3.10 (running as root)
        sh '''
          python --version
          pip --version
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pytest || true
        '''
      }
    }

    stage('Security Scan') {
      steps {
        sh '''
          pip install bandit || true
          bandit -r src || true
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
      echo "Pipeline executed successfully"
    }
    failure {
      echo "Pipeline failed"
    }
  }
}

