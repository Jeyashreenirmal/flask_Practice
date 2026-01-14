pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '-u root'
        }
    }

    environment {
        MONGO_URI    = credentials('mongo-uri')
        SECRET_KEY   = credentials('secret-key')
        GITHUB_TOKEN = credentials('github-tokenn')
    }

    stages {

        stage('Build') {
            steps {
                sh '''
                    python --version
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    echo "Deploy stage completed"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
