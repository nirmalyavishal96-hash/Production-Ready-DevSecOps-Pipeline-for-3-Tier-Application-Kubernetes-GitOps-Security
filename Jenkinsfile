pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "nirmalyavishal97/devsecops-flask-app"
        DOCKER_CREDENTIALS_ID = "dockerhub-creds"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nirmalyavishal96-hash/Project4-Devsecops-3tier-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} .
                docker tag ${DOCKER_IMAGE}:${IMAGE_TAG} ${DOCKER_IMAGE}:latest
                """
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh """
                trivy image --exit-code 1 --severity HIGH,CRITICAL ${DOCKER_IMAGE}:${IMAGE_TAG}
                """
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh """
                    echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin
                    docker push ${DOCKER_IMAGE}:${IMAGE_TAG}
                    docker push ${DOCKER_IMAGE}:latest
                    """
                }
            }
        }

        stage('Update Helm values.yaml') {
            steps {
                sh """
                sed -i 's/tag:.*/tag: "${IMAGE_TAG}"/' flask-chart/values.yaml
                """
            }
        }

        stage('Commit Helm Update') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'github-creds',
                    usernameVariable: 'GIT_USER',
                    passwordVariable: 'GIT_PASS'
                )]) {

                    sh """
                    git config user.email "jenkins@local"
                    git config user.name "jenkins"

                    git add flask-chart/values.yaml
                    git commit -m "Update image tag to ${IMAGE_TAG}" || echo "No changes"

                    git push https://\$GIT_USER:\$GIT_PASS@github.com/nirmalyavishal96-hash/Project4-Devsecops-3tier-app.git HEAD:main
                    """
                }
            }
        }
    }
}