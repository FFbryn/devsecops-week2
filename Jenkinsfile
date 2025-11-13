pipeline {
  agent {
    docker {
      image 'python:3.10'
      args '-u root:root' // optional: jalankan sebagai root supaya bisa install jika perlu
    }
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Setup') {
      steps {
        sh 'python --version'
        sh 'pip --version'
        // buat virtualenv opsional, tapi cukup install paket di lingkungan container
        sh 'pip install --upgrade pip'
        sh 'pip install -r requirements.txt || true'
        sh 'pip install pytest bandit junit-xml || true'
      }
    }

    stage('Test') {
      steps {
        sh 'pytest --junitxml=reports/results.xml || true'
      }
      post {
        always {
          junit allowEmptyResults: true, testResults: 'reports/results.xml'
        }
      }
    }

    stage('Security Scan') {
      steps {
        sh 'bandit -r . -f xml -o reports/bandit.xml || true'
        archiveArtifacts artifacts: 'reports/**', fingerprint: true
      }
    }
  }

  post {
    success { echo 'Pipeline sukses' }
    failure { echo 'Pipeline gagal' }
  }
}

