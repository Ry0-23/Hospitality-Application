pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = "harshhhh23/hospitality-app"
        APP_EC2 = "ubuntu@34.229.195.51"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                sh "docker push ${IMAGE_NAME}:${BUILD_NUMBER}"
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy to App EC2') {
            steps {
                sh """
                    ssh -o StrictHostKeyChecking=no ${APP_EC2} '
                        docker pull harshhhh23/hospitality-app:latest &&
                        docker stop hospitality-app || true &&
                        docker rm hospitality-app || true &&
                        docker run -d \
                            --name hospitality-app \
                            --restart always \
                            -p 5000:5000 \
                            harshhhh23/hospitality-app:latest
                    '
                """
            }
        }

        stage('Cleanup') {
            steps {
                sh "docker rmi ${IMAGE_NAME}:${BUILD_NUMBER} || true"
                sh "docker rmi ${IMAGE_NAME}:latest || true"
            }
        }
    }

    post {
        success {
            echo "Deployed harshhhh23/hospitality-app:${BUILD_NUMBER} to App EC2 successfully!"
        }
        failure {
            echo "Pipeline failed — check the console output above"
        }
    }
}