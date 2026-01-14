pipeline {
    agent any

    environment {
        MONGO_URI    = credentials('mongo-uri')
        SECRET_KEY   = credentials('secret-key')
        GITHUB_TOKEN = credentials('github-tokenn')
    }

    stages {

        stage('Build') {
            steps {
                sh '''
                    python3 --version
                    python3 -m pip --version || echo "pip module not available"
                    python3 -m pip install --user --upgrade pip
                    python3 -m pip install --user -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    export PATH=$HOME/.local/bin:$PATH
                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    echo "Deploy step completed"
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
