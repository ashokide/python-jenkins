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