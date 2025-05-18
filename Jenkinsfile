pipeline {
    agent any

    stages {
        stage('Checkout'){
            checkout scm
        }
        stage ('Test') {
            steps {
                echo "Starting the Test Stage"
                sh 'python3 -m pytest test.py'
            }
        }
    }
}