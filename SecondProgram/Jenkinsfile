pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                echo "Building Docker image"
                bat "docker build -t mydockerapp:t1 ."
            }
        }

        stage('Login') {
            steps {
                echo "Logging in to Docker Hub"
                bat "docker login -u sreeshvini4 -p sreeshvini"
            }
        }

        stage('Run') {
            steps {
                echo "Running container"
                bat "docker rm -f project1 || exit 0"
                bat "docker run -d -p 3000:3000 --name project1 mydockerapp:t1"
            }
        }

        stage('Push') {
            steps {
                echo "Pushing to Docker Hub"
                bat "docker tag mydockerapp:t1 sreeshvini4/sample1:t1"
                bat "docker push sreeshvini4/sample1:t1"
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}
