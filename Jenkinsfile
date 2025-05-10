pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = "sayalipawar1264"
        APP_NAME = "docker_repo1"  
        IMAGE_TAG = "${BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}/${APP_NAME}"
        REGISTRY_CREDS = 'dockerhub'
    }
    stages {
        stage('Cleanup workspace') {
            steps {
                script {
                    cleanWs()
                }
            }
        }
        stage('Checkout SCM') {
            steps {
                git credentialsId: 'github',
                    url: 'https://github.com/sayali1264/gitops-argocd-project2.git',
                    branch: 'main'
            }
        }
         stage('Build Docker Image') {
            steps {
                script {
                    docker_image = docker.build("${IMAGE_NAME}")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', REGISTRY_CREDS) {
                        docker_image.push("$BUILD_NUMBER")
                        docker_image.push('latest')
                    }
                }
            }
        }


    stage('Updating kubernetes deployment file') {
            steps {
                script {
                    sh """
                        cat flask-deployment.yaml
                        sed -i 's/${APP_NAME}.*/${APP_NAME}:${IMAGE_TAG}/g' flask-deployment.yaml
                        cat flask-deployment.yaml
                    """
                }
            }
        }


    }
}
