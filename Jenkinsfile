@Library('pipeline-library@master')
import com.genesys.jenkins.CI

timeout(150) {
    node('dev_mesos_v2||dev_shared_v2') {
        LIBRARY = "recognizers-text"
        LIBRARY_FOLDER = "Recognizers-Text/Python"

        stage('Clean Checkout') {
        retry(3){
          checkout scm
          COMMIT_ID = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
          BRANCH = sh(returnStdout: true, script: "git branch -r --contains ${COMMIT_ID}").trim().split('/')[-1]
          COMMIT_TAG = sh(returnStdout: true, script: "(git describe --exact-match ${COMMIT_ID}) 2> /dev/null || git show-ref --tags -d | grep ^${COMMIT_ID} | sed -e 's,.* refs/tags/,,' -e 's/\\^{}//' | xargs || echo ''").trim()
          if(BRANCH.equals("master")) {
            NICKNAME = 'main'
          } else {
            NICKNAME = 'PR'
          }
          sh "echo ${NICKNAME}"
          sh """
          rm -rf allure-results
          mkdir allure-results
          """
          withCredentials([usernamePassword(credentialsId: params.CREDENTIALSID, usernameVariable: 'user', passwordVariable: 'password')]) {
            sh """
            rm -rf pip.conf
            echo '[global]' >> pip.conf
            echo 'extra-index-url = https://$user:$password@purecloud.jfrog.io/purecloud/api/pypi/inin-pypi/simple' >> pip.conf
            """
          }

        }
      }

        stage("Test install package and run tests") {
            sh """
                virtualenv -p python3.8 --clear venv
                . venv/bin/activate
                build.sh venv
                """
        }

//         stage("Publish Build Artifacts") {
//             dir(LIBRARY_FOLDER){
//                 try {
//                     sh """
//                     virtualenv -p python3.8 --clear venv
//                     . venv/bin/activate
//                     python ./libraries/recognizers-text/setup.py sdist upload -r inin-pypi
//                     python ./libraries/recognizers-number/setup.py sdist upload -r inin-pypi
//                     python ./libraries/recognizers-number-with-unit/setup.py sdist upload -r inin-pypi
//                     python ./libraries/datatypes-timex-expression/setup.py sdist upload -r inin-pypi
//                     python ./libraries/recognizers-date-time/setup.py sdist upload -r inin-pypi
//                     python ./libraries/recognizers-sequence/setup.py sdist upload -r inin-pypi
//                     python ./libraries/recognizers-choice/setup.py sdist upload -r inin-pypi
//                     python ./libraries/recognizers-suite/setup.py sdist upload -r inin-pypi
//                     """
//                 } catch(Exception e) {
//                     echo "Skipping publish of artifact version ${ARTIFACT_VERSION}. Exception is ${e}"
//                 }
//             }
//         }

    }
}
