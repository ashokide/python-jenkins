pipeline {
    agent any

    stages {
        stage('Checkout'){
            steps {
                echo "Checkout Stage"
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'ef9fabce-3d67-4dcb-9824-cf12e6129936', url: 'https://github.com/ashokide/python-jenkins.git']])   
            }
        }
        stage ('Test') {
            steps {
                echo "Test Stage"
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pytest test.py'
            }
        }
        stage ('Build and Push Docker Image'){
            steps {
                echo "Build and Push Docker Image Stage"
                script{
                    withDockerRegistry(credentialsId: '295939a3-9ace-404f-b31b-1bb41723ebdd', url: 'https://registry.hub.docker.com') {
                        sh "docker build -t ashok2001/python-jenkins:${env.BUILD_ID} ."
                        sh "docker push ashok2001/python-jenkins:${env.BUILD_ID}"
                    }
                }
            }
        }
    }
}