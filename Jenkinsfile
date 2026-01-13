pipeline {
    agent any

    environment {
        // These should ideally come from Jenkins Credentials
        MONGO_URI  = credentials('mongo-uri')
        SECRET_KEY = credentials('secret-key')
    }

    stages {

        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    source venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    source venv/bin/activate
                    echo "Deploying application to staging..."
                    python app.py
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
