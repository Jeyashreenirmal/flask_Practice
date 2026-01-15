pipeline {
    agent any

    environment {
        // These should ideally come from Jenkins Credentials
        MONGO_URI  = credentials('mongo-uri')
        SECRET_KEY = credentials('secret-key')
        GITHUB_TOKEN = credentials('github-tokenn')
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
                    echo "Deploy stage placeholder (no long-running server in CI)"
                '''
            }
        }
    }

    post {
        success {
            mail to: 'jsree261997@gmail.com',
                 subject: "Jenkins SUCCESS: ${env.JOB_NAME}",
                 body: "Build ${env.BUILD_NUMBER} succeeded."
        }
        failure {
            mail to: 'jsree261997@gmail.com',
                 subject: "Jenkins FAILED: ${env.JOB_NAME}",
                 body: "Build ${env.BUILD_NUMBER} failed. Check Jenkins logs."
        }
    }
}
