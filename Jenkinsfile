pipeline {
    agent any;
    
    stages {
        stage("Code") {
            steps {
            git url: 'https://github.com/yo-its-anas/flask-app.git', branch: 'main'
            }
        }
        stage("Build") {
            steps {
            sh 'docker build -t flask-app .'
            }
        }
        stage("Test") {
            steps {
            echo "Test stage done..."
            }
        }
        stage("Push to Docker Hub") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId:'dockerhubcreds',
                    usernameVariable:'dockerHubUser',
                    passwordVariable:'dockerHubPass')]){
                        sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                        sh "docker image tag flask-app ${env.dockerHubUser}/flask-app:latest"
                        sh "docker push ${env.dockerHubUser}/flask-app:latest"
                    }
            }
        }
        stage("Deployment") {
            steps { 
            sh "docker-compose down"    
            sh "docker-compose up --build -d"
                
            }
        }
    }
}
