pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
        timestamps()
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/jschuangcpp/jenkins-webex-cicd.git'
            }
        }

        stage('Build') {
            steps {
                sh 'chmod +x build.sh'
                sh './build.sh'
            }
        }

        stage('Test') {
            steps {
                sh 'chmod +x test.sh'
                sh './test.sh'
            }
        }
    }

    post {
        success {
            script {
                sendWebex('SUCCESS')
            }
        }

        failure {
            script {
                sendWebex('FAILURE')
            }
        }
    }
}


def sendWebex(String status) {
    withCredentials([
        string(
            credentialsId: 'webex-bot-token',
            variable: 'WEBEX_BOT_TOKEN'
        ),
        string(
            credentialsId: 'webex-room-id',
            variable: 'WEBEX_ROOM_ID'
        )
    ]) {
        withEnv(["WEBEX_BUILD_STATUS=${status}"]) {
            sh 'python3 notify_webex.py'
        }
    }
}