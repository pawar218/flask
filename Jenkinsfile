pipeline{
    agent any
   
    stages{
        stage('SCM Checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/pawar218/flask.git'
            }
        }
        stage('docker image build'){
            steps{
                sh '/usr/bin/docker image build -t shubhangi218/python .'
            }
        }
        stage('docker auth'){
            steps{
                sh 'echo dckr_pat_xP0tvLwbx8dszBEkQwyHIWEGqYw | /usr/bin/docker login -u shubhangi218 --password-stdin'
            }
        }
        stage('docker image push'){
            steps{
                sh '/usr/bin/docker image push shubhangi218/python'
            }
        }
        stage('delivery confirmation'){
            steps{
                input 'Do you want to deploy  application'
            }
        }
        stage('docker remove service'){
            steps{
                sh '/usr/bin/docker service rm flaskservice'
            }
        }
        stage('docker create service'){
            steps{
                sh '/usr/bin/docker service create --name service2 --replicas 2 -p 4000:4000 shubhangi218/python'
            }
        }

    }
}

  
