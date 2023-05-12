pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "maramkh11/scores:latest"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']],
                         doGenerateSubmoduleConfigurations: false,
                         extensions: [],
                         submoduleCfg: [],
                         userRemoteConfigs: [[url: 'https://github.com/maramkh11/world_of_games.git']]])
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    sh 'docker run -d -p 8777:8777 -v .:/MainScores.py $DOCKER_IMAGE'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'python /tests/e2e.py'
                }
            }
            post {
                always {
                    script {
                        sh 'docker stop $(docker ps -q --filter ancestor=$DOCKER_IMAGE)'
                    }
                }
                success {
                    script {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
                failure {
                    error "Tests failed"
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
    }
}
