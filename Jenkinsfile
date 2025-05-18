pipeline {
    agent any

    stages {
        stage('Checkout'){
            steps {
             checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'ef9fabce-3d67-4dcb-9824-cf12e6129936', url: 'https://github.com/ashokide/python-jenkins.git']])   
            }
        }
        stage ('Test') {
            steps {
                echo "Starting the Test Stage"
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pytest test.py'
            }
        }
        stage ('Build Docker Image'){
            steps {
                script{
                    docker.withRegistry('https://registry.example.com', '295939a3-9ace-404f-b31b-1bb41723ebdd	') {
                        def pythonJenkins = docker.build("python-jenkins:${env.BUILD_ID}")
                        pythonJenkins.push()
                    }
                }
            }
        }
        stage ('Push to Docker Hub') {
            steps {
                echo "Pushing to Docker Hub"
                
            }

        }
    }

    post {
            success {
                echo "Test Stage completed successfully"
            }

            failure {
                echo "Test Stage failed"
            }
    }
}