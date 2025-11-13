pipeline {
  agent any
  tools { python 'python3' } // optional jika sudah terkonfigurasi di Jenkins
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install Dependencies') {
      steps {
        sh '''
          python3 -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
          pip install pytest bandit
        '''
      }
    }
    stage('Unit Tests') {
      steps {
        sh 'pytest --maxfail=1 --disable-warnings -q'
      }
      post {
        always {
          junit '**/test-results/*.xml'  || echo 'junit not produced'
        }
      }
    }
    stage('Security Scan') {
      steps {
        sh 'bandit -r . || true'
      }
    }
    stage('Deploy (simulate)') {
      when { branch 'main' }
      steps {
        sh 'echo "Deploying to staging (simulated)..."'
      }
    }
  }
  post {
    success { echo 'Pipeline succeeded' }
    failure { echo 'Pipeline failed' }
  }
}

