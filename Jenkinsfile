pipeline {
  agent any

  stages {
    stage('Checkout') { steps { checkout scm } }

    stage('Run tests in Python container') {
      steps {
        sh '''
          docker run --rm -v "$PWD":/workspace -w /workspace python:3.10 bash -lc "
          pip install -r requirements.txt pytest bandit || true &&
          pytest --maxfail=1 --disable-warnings -q
          "
        '''
      }
    }

    stage('Security Scan') {
      steps {
        sh '''
          docker run --rm -v "$PWD":/workspace -w /workspace python:3.10 bash -lc "
          pip install bandit || true &&
          bandit -r . -o bandit-report.txt || true
          "
        '''
        archiveArtifacts artifacts: 'bandit-report.txt'
      }
    }
  }
}

