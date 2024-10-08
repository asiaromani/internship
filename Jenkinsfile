pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t myapp_image .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run myapp_image pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s-deployment.yml'
            }
        }
    }
}

