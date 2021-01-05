pipeline {
    agent {
        docker {
            image 'python' 
            args '-v /root/.m2:/root/.m2' 
        }
    }
    stages {
        stage('Set Up') {
            steps {
                script {
                    sh 'rm -rf jenkins.python.unittest_python-fundamentals'
                }
            }
        }
        stage('SCM Checkout') {
            steps {
                sh 'git clone https://github.com/nmm131/jenkins.python.unittest_python-fundamentals.git'
            }
        }
        stage('Compile-Package-Test') {
            steps {
                script {
                    dir('./jenkins.python.unittest_python-fundamentals') {
                        sh "python -m unittest discover -s ./src/test/ -p '*_test.py'"
                    }
                }
            }
        }
    }
}
