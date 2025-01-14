pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Clone your Git repository
                git branch: 'main', url: 'https://github.com/Mariam233-hhm/event-producer.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install pika'
            }
        }
        stage('Run Producer') {
            steps {
                // Run the producer script
                sh 'python producer.py'
            }
        }
        stage('Run Consumer') {
            steps {
                // Run the consumer script
                sh 'python consumer.py & sleep 5'
            }
        }
    }
}