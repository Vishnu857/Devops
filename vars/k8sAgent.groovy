def call(Map config = [:]) {
    return [
        cloud: config.cloud ?: 'deploy',
        inheritFrom: config.podTemplate,
        defaultContainer: config.containerName ?: 'jnlp',
        serviceAccount: config.serviceAccount ?: 'jenkins'
    ]
}
