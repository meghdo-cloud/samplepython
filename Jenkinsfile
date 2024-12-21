library identifier: 'pythonPipeline@main', retriever: modernSCM([$class: 'GitSCMSource',
    remote: 'git@github.com:meghdo-cloud/shared-libraries.git',
    credentialsId: 'jenkins_agent_ssh'])
pythonPipeline (
    projectId: "meghdo-4567",
    clusterName: "meghdo-cluster",
    clusterRegion: "europe-west1",
    appName: "drizzle-python",
    dockerRegistry: "europe-west1-docker.pkg.dev",
    namespace: "default",
    scanOWASP: "false"  // OWASP Scanning takes about 7-10 min of scanning time, turn on when scanning is needed
)