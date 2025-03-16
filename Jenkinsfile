library identifier: 'awscommonPipeline@main', retriever: modernSCM([$class: 'GitSCMSource',
    remote: 'git@github.com:meghdo-cloud/shared-libraries.git',
    credentialsId: 'jenkins_agent_ssh'])
commonPipeline (
    accountName: "meghdo"
    accountId: "354918396806"
    clusterName: "meghdo-cluster",
    region: "us-east-1",
    appName: "samplepython",
    namespace: "default",
    scanOWASP: "false",  // OWASP Scanning takes about 7-10 min of scanning time, turn on when scanning is needed
    label: 'python'
) {
    container('python') { 
      sh """
      python -m venv venv                  # Create virtual environment
      . venv/bin/activate                  # Activate virtual environment
      pip install -r requirements.txt      # Install dependencies
      """
    }
}   
