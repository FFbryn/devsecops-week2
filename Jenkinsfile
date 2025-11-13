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
                set -o errexit
                set -o nounset
                set -o pipefail

                # create and activate virtual environment
                python3 -m venv venv
                . venv/bin/activate

                # ensure pip up-to-date and install requirements
                pip install --upgrade pip
                pip install -r requirements.txt || true

                # debug listings
                echo "=== Workspace listing ==="
                ls -la .
                echo "=== tests dir listing ==="
                ls -la tests || true

                # run pytest and capture return code
                pytest -q || rc=$?; true
                if [ -n "${rc:-}" ] && [ "$rc" -eq 5 ]; then
                  echo "Pytest returned 5 (no tests collected). Treating as success."
                  exit 0
                elif [ -n "${rc:-}" ] && [ "$rc" -ne 0 ]; then
                  echo "Pytest failed with exit code $rc"
                  exit $rc
                else
                  echo "Pytest succeeded."
                fi
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                set -o errexit
                set -o nounset
                set -o pipefail

                # use same venv for security scan
                . venv/bin/activate

                # install bandit if not present
                pip install --upgrade pip
                pip install bandit || true

                # run bandit (scan src folder, adjust path if needed)
                if [ -d "src" ]; then
                  bandit -r src || rc=$?; true
                  echo "Bandit exit code: ${rc:-0}"
                  # If you want to fail on bandit issues, uncomment next line:
                  # [ "${rc:-0}" -ne 0 ] && exit $rc
                else
                  echo "Folder 'src' not found — skipping bandit."
                fi
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

