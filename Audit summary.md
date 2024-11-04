# Audit summary

Summary for [Jenkins instance](http://10.63.20.41:8080/)

- GitHub Actions Importer version: **1.3.22189 (3d66e3fa31c29fcd961bcfeb0bd291af5b11cc49)**
- Performed at: **10/16/24 at 08:29**

## Pipelines

Total: **119**

- Successful: **76 (63%)**
- Partially successful: **37 (31%)**
- Unsupported: **0 (0%)**
- Failed: **6 (5%)**

### Job types

Supported: **119 (100%)**

- flow-definition: **118**
- project: **1**

### Build steps

Total: **508**

Known: **106 (20%)**

- sh: **56**
- echo: **19**
- archiveArtifacts: **10**
- git: **8**
- cleanWs: **5**
- build: **3**
- checkout: **3**
- junit: **1**
- hudson.tasks.Shell: **1**

Unknown: **40 (7%)**

- ansibleTower: **26**
- updateJiraStatus: **4**
- sleep: **3**
- withSonarQubeEnv: **3**
- gitclone: **2**
- dependencyCheckPublisher: **1**
- dependencyCheck: **1**

Unsupported: **362 (71%)**

- script: **361**
- emailext: **1**

Actions: **559**

- actions/checkout@v4.1.0: **436**
- run: **109**
- actions/upload-artifact@v4.1.0: **10**
- octokit/request-action@v2.1.9: **3**
- EnricoMi/publish-unit-test-result-action@v2.12.0: **1**

### Triggers

Total: **82**

Known: **82 (100%)**

- hudson.model.ParametersDefinitionProperty: **50**
- com.dabsquared.gitlabjenkins.GitLabPushTrigger: **29**
- hudson.triggers.SCMTrigger: **3**

Actions: **188**

- workflow_dispatch: **124**
- push: **32**
- pull_request: **29**
- schedule: **3**

### Environment

Total: **173**

Known: **94 (54%)**

- NAMESPACE: **35**
- Owner: **11**
- mailID: **11**
- key_name: **5**
- kubeconfig: **3**
- usersLoad: **3**
- amiId: **2**
- instance_id: **2**
- trivy_server_url: **2**
- trivy_server_token: **2**
- statusURL: **1**
- LanguageSection: **1**
- SONARQUBE_PROJECT_KEY: **1**
- SONARQUBE_SERVER: **1**
- sonarurl: **1**
- giturl: **1**
- nexusurl: **1**
- baseURL: **1**
- restIP: **1**
- restPORT: **1**
- registry_pass: **1**
- registry_user: **1**
- namespace: **1**
- HELM_RELEASE_NAME: **1**
- kubeConfigPath: **1**
- SONAR_HOST_URL: **1**
- jenkins_url: **1**
- registry_url: **1**

Unknown: **79 (45%)**

- restIP: **14**
- restPORT: **14**
- NAMESPACE: **5**
- Storage_size: **4**
- PATH: **3**
- KREW_ROOT: **3**
- name: **3**
- instanceType: **3**
- instance_count: **3**
- maxResponseTime: **3**
- frontUrl: **3**
- appName: **3**
- hostName: **2**
- errorThreshold: **2**
- namespace: **2**
- maxErrorPercent: **1**
- hostname: **1**
- frontEndService: **1**
- promUrl: **1**
- baseURL: **1**
- minReqRate: **1**
- frontService: **1**
- REGISTRY_CREDENTIALS: **1**
- SONAR_TOKEN: **1**
- SONARQUBE_TOKEN: **1**
- PE_IP: **1**
- restDNS: **1**

Actions: **94**

- NAMESPACE: **35**
- Owner: **11**
- mailID: **11**
- key_name: **5**
- kubeconfig: **3**
- usersLoad: **3**
- amiId: **2**
- instance_id: **2**
- trivy_server_url: **2**
- trivy_server_token: **2**
- statusURL: **1**
- LanguageSection: **1**
- SONARQUBE_PROJECT_KEY: **1**
- SONARQUBE_SERVER: **1**
- sonarurl: **1**
- giturl: **1**
- nexusurl: **1**
- baseURL: **1**
- restIP: **1**
- restPORT: **1**
- registry_pass: **1**
- registry_user: **1**
- namespace: **1**
- HELM_RELEASE_NAME: **1**
- kubeConfigPath: **1**
- SONAR_HOST_URL: **1**
- jenkins_url: **1**
- registry_url: **1**

### Other

Total: **1**

Unknown: **1 (100%)**

- timestamps: **1**

### Manual tasks

Total: **310**

Self hosted runners: **310**

- `master`: **283**
- `loadgenerator`: **1**
- `pe-demo`: **4**
- `llama`: **2**
- `mddp`: **5**
- `opa`: **9**
- `marvel-trainees-syam`: **3**
- `kubernetes`: **2**
- `platformeng`: **1**

### Successful

#### AI

- [AI/.github/workflows/ai.yml](AI/.github/workflows/ai.yml)
- [AI/config.json](AI/config.json)
- [AI/jenkinsfile](AI/jenkinsfile)

#### airflow-test

- [airflow-test/.github/workflows/airflow-test.yml](airflow-test/.github/workflows/airflow-test.yml)
- [airflow-test/config.json](airflow-test/config.json)
- [airflow-test/jenkinsfile](airflow-test/jenkinsfile)

#### AppDeployment

- [AppDeployment/.github/workflows/appdeployment.yml](AppDeployment/.github/workflows/appdeployment.yml)
- [AppDeployment/config.json](AppDeployment/config.json)
- [AppDeployment/jenkinsfile](AppDeployment/jenkinsfile)

#### auctane

- [auctane/.github/workflows/auctane.yml](auctane/.github/workflows/auctane.yml)
- [auctane/config.json](auctane/config.json)
- [auctane/jenkinsfile](auctane/jenkinsfile)

#### AutoFix_Log_Analysis

- [AutoFix_Log_Analysis/.github/workflows/autofix_log_analysis.yml](AutoFix_Log_Analysis/.github/workflows/autofix_log_analysis.yml)
- [AutoFix_Log_Analysis/config.json](AutoFix_Log_Analysis/config.json)
- [AutoFix_Log_Analysis/jenkinsfile](AutoFix_Log_Analysis/jenkinsfile)

#### aws-metrics

- [aws-metrics/.github/workflows/aws-metrics.yml](aws-metrics/.github/workflows/aws-metrics.yml)
- [aws-metrics/config.json](aws-metrics/config.json)
- [aws-metrics/jenkinsfile](aws-metrics/jenkinsfile)

#### aws_infra

- [aws_infra/.github/workflows/aws_infra.yml](aws_infra/.github/workflows/aws_infra.yml)
- [aws_infra/config.json](aws_infra/config.json)
- [aws_infra/jenkinsfile](aws_infra/jenkinsfile)

#### aws_jump_box

- [aws_jump_box/.github/workflows/aws_jump_box.yml](aws_jump_box/.github/workflows/aws_jump_box.yml)
- [aws_jump_box/config.json](aws_jump_box/config.json)
- [aws_jump_box/jenkinsfile](aws_jump_box/jenkinsfile)

#### aws_private_instance

- [aws_private_instance/.github/workflows/aws_private_instance.yml](aws_private_instance/.github/workflows/aws_private_instance.yml)
- [aws_private_instance/config.json](aws_private_instance/config.json)
- [aws_private_instance/jenkinsfile](aws_private_instance/jenkinsfile)

#### Azure_Infra

- [Azure_Infra/.github/workflows/azure_infra.yml](Azure_Infra/.github/workflows/azure_infra.yml)
- [Azure_Infra/config.json](Azure_Infra/config.json)
- [Azure_Infra/jenkinsfile](Azure_Infra/jenkinsfile)

#### BigDataCluster

- [BigDataCluster/.github/workflows/bigdatacluster.yml](BigDataCluster/.github/workflows/bigdatacluster.yml)
- [BigDataCluster/config.json](BigDataCluster/config.json)
- [BigDataCluster/jenkinsfile](BigDataCluster/jenkinsfile)

#### BigDataCluster2

- [BigDataCluster2/.github/workflows/bigdatacluster2.yml](BigDataCluster2/.github/workflows/bigdatacluster2.yml)
- [BigDataCluster2/config.json](BigDataCluster2/config.json)
- [BigDataCluster2/jenkinsfile](BigDataCluster2/jenkinsfile)

#### bigtop

- [bigtop/.github/workflows/bigtop.yml](bigtop/.github/workflows/bigtop.yml)
- [bigtop/config.json](bigtop/config.json)
- [bigtop/jenkinsfile](bigtop/jenkinsfile)

#### chaos

- [chaos/.github/workflows/chaos.yml](chaos/.github/workflows/chaos.yml)
- [chaos/config.json](chaos/config.json)
- [chaos/jenkinsfile](chaos/jenkinsfile)

#### cisco

- [cisco/.github/workflows/cisco.yml](cisco/.github/workflows/cisco.yml)
- [cisco/config.json](cisco/config.json)
- [cisco/jenkinsfile](cisco/jenkinsfile)

#### cisco_rollback

- [cisco_rollback/.github/workflows/cisco_rollback.yml](cisco_rollback/.github/workflows/cisco_rollback.yml)
- [cisco_rollback/config.json](cisco_rollback/config.json)
- [cisco_rollback/jenkinsfile](cisco_rollback/jenkinsfile)

#### cluster-provisioning

- [cluster-provisioning/.github/workflows/cluster-provisioning.yml](cluster-provisioning/.github/workflows/cluster-provisioning.yml)
- [cluster-provisioning/config.json](cluster-provisioning/config.json)
- [cluster-provisioning/jenkinsfile](cluster-provisioning/jenkinsfile)

#### Code_Coverage

- [Code_Coverage/.github/workflows/code_coverage.yml](Code_Coverage/.github/workflows/code_coverage.yml)
- [Code_Coverage/config.json](Code_Coverage/config.json)
- [Code_Coverage/jenkinsfile](Code_Coverage/jenkinsfile)

#### Code_Documentation

- [Code_Documentation/.github/workflows/code_documentation.yml](Code_Documentation/.github/workflows/code_documentation.yml)
- [Code_Documentation/config.json](Code_Documentation/config.json)
- [Code_Documentation/jenkinsfile](Code_Documentation/jenkinsfile)

#### Code_Optimization

- [Code_Optimization/.github/workflows/code_optimization.yml](Code_Optimization/.github/workflows/code_optimization.yml)
- [Code_Optimization/config.json](Code_Optimization/config.json)
- [Code_Optimization/jenkinsfile](Code_Optimization/jenkinsfile)

#### cost_test

- [cost_test/.github/workflows/cost_test.yml](cost_test/.github/workflows/cost_test.yml)
- [cost_test/config.json](cost_test/config.json)
- [cost_test/jenkinsfile](cost_test/jenkinsfile)

#### dbprovision

- [dbprovision/.github/workflows/dbprovision.yml](dbprovision/.github/workflows/dbprovision.yml)
- [dbprovision/config.json](dbprovision/config.json)
- [dbprovision/jenkinsfile](dbprovision/jenkinsfile)

#### Docker

- [Docker/.github/workflows/docker.yml](Docker/.github/workflows/docker.yml)
- [Docker/config.json](Docker/config.json)
- [Docker/jenkinsfile](Docker/jenkinsfile)

#### ecocode-java

- [ecocode-java/.github/workflows/ecocode-java.yml](ecocode-java/.github/workflows/ecocode-java.yml)
- [ecocode-java/config.json](ecocode-java/config.json)
- [ecocode-java/jenkinsfile](ecocode-java/jenkinsfile)

#### enc-dec

- [enc-dec/.github/workflows/enc-dec.yml](enc-dec/.github/workflows/enc-dec.yml)
- [enc-dec/config.json](enc-dec/config.json)
- [enc-dec/jenkinsfile](enc-dec/jenkinsfile)

#### encrypt-decrypt

- [encrypt-decrypt/.github/workflows/encrypt-decrypt.yml](encrypt-decrypt/.github/workflows/encrypt-decrypt.yml)
- [encrypt-decrypt/config.json](encrypt-decrypt/config.json)
- [encrypt-decrypt/jenkinsfile](encrypt-decrypt/jenkinsfile)

#### GenAI_POC

- [GenAI_POC/.github/workflows/genai_poc.yml](GenAI_POC/.github/workflows/genai_poc.yml)
- [GenAI_POC/config.json](GenAI_POC/config.json)
- [GenAI_POC/jenkinsfile](GenAI_POC/jenkinsfile)

#### gradle

- [gradle/.github/workflows/gradle.yml](gradle/.github/workflows/gradle.yml)
- [gradle/config.json](gradle/config.json)
- [gradle/jenkinsfile](gradle/jenkinsfile)

#### intel_parallel

- [intel_parallel/.github/workflows/intel_parallel.yml](intel_parallel/.github/workflows/intel_parallel.yml)
- [intel_parallel/config.json](intel_parallel/config.json)
- [intel_parallel/jenkinsfile](intel_parallel/jenkinsfile)

#### Intel_RFI

- [Intel_RFI/.github/workflows/intel_rfi.yml](Intel_RFI/.github/workflows/intel_rfi.yml)
- [Intel_RFI/config.json](Intel_RFI/config.json)
- [Intel_RFI/jenkinsfile](Intel_RFI/jenkinsfile)

#### intelPacker

- [intelPacker/.github/workflows/intelpacker.yml](intelPacker/.github/workflows/intelpacker.yml)
- [intelPacker/config.json](intelPacker/config.json)
- [intelPacker/jenkinsfile](intelPacker/jenkinsfile)

#### jaeger

- [jaeger/.github/workflows/jaeger.yml](jaeger/.github/workflows/jaeger.yml)
- [jaeger/config.json](jaeger/config.json)
- [jaeger/jenkinsfile](jaeger/jenkinsfile)

#### kube-hunter

- [kube-hunter/.github/workflows/kube-hunter.yml](kube-hunter/.github/workflows/kube-hunter.yml)
- [kube-hunter/config.json](kube-hunter/config.json)
- [kube-hunter/jenkinsfile](kube-hunter/jenkinsfile)

#### languageConversion

- [languageConversion/.github/workflows/languageconversion.yml](languageConversion/.github/workflows/languageconversion.yml)
- [languageConversion/config.json](languageConversion/config.json)
- [languageConversion/jenkinsfile](languageConversion/jenkinsfile)

#### LifeCycle

- [LifeCycle/.github/workflows/lifecycle.yml](LifeCycle/.github/workflows/lifecycle.yml)
- [LifeCycle/config.json](LifeCycle/config.json)
- [LifeCycle/jenkinsfile](LifeCycle/jenkinsfile)

#### LLM

- [LLM/.github/workflows/llm.yml](LLM/.github/workflows/llm.yml)
- [LLM/config.json](LLM/config.json)
- [LLM/jenkinsfile](LLM/jenkinsfile)

#### Log_Analysis

- [Log_Analysis/.github/workflows/log_analysis.yml](Log_Analysis/.github/workflows/log_analysis.yml)
- [Log_Analysis/config.json](Log_Analysis/config.json)
- [Log_Analysis/jenkinsfile](Log_Analysis/jenkinsfile)

#### mddp-alarm-manager

- [mddp-alarm-manager/.github/workflows/mddp-alarm-manager.yml](mddp-alarm-manager/.github/workflows/mddp-alarm-manager.yml)
- [mddp-alarm-manager/config.json](mddp-alarm-manager/config.json)
- [mddp-alarm-manager/jenkinsfile](mddp-alarm-manager/jenkinsfile)

#### mddp-caching-helm

- [mddp-caching-helm/.github/workflows/mddp-caching-helm.yml](mddp-caching-helm/.github/workflows/mddp-caching-helm.yml)
- [mddp-caching-helm/config.json](mddp-caching-helm/config.json)
- [mddp-caching-helm/jenkinsfile](mddp-caching-helm/jenkinsfile)

#### mddp-efk-logging

- [mddp-efk-logging/.github/workflows/mddp-efk-logging.yml](mddp-efk-logging/.github/workflows/mddp-efk-logging.yml)
- [mddp-efk-logging/config.json](mddp-efk-logging/config.json)
- [mddp-efk-logging/jenkinsfile](mddp-efk-logging/jenkinsfile)

#### mddp-enc-dec-helm

- [mddp-enc-dec-helm/.github/workflows/mddp-enc-dec-helm.yml](mddp-enc-dec-helm/.github/workflows/mddp-enc-dec-helm.yml)
- [mddp-enc-dec-helm/config.json](mddp-enc-dec-helm/config.json)
- [mddp-enc-dec-helm/jenkinsfile](mddp-enc-dec-helm/jenkinsfile)

#### mddp-encrypt-decrypt

- [mddp-encrypt-decrypt/.github/workflows/mddp-encrypt-decrypt.yml](mddp-encrypt-decrypt/.github/workflows/mddp-encrypt-decrypt.yml)
- [mddp-encrypt-decrypt/config.json](mddp-encrypt-decrypt/config.json)
- [mddp-encrypt-decrypt/jenkinsfile](mddp-encrypt-decrypt/jenkinsfile)

#### mddp-jaeger

- [mddp-jaeger/.github/workflows/mddp-jaeger.yml](mddp-jaeger/.github/workflows/mddp-jaeger.yml)
- [mddp-jaeger/config.json](mddp-jaeger/config.json)
- [mddp-jaeger/jenkinsfile](mddp-jaeger/jenkinsfile)

#### mddp-license-mgmt

- [mddp-license-mgmt/.github/workflows/mddp-license-mgmt.yml](mddp-license-mgmt/.github/workflows/mddp-license-mgmt.yml)
- [mddp-license-mgmt/config.json](mddp-license-mgmt/config.json)
- [mddp-license-mgmt/jenkinsfile](mddp-license-mgmt/jenkinsfile)

#### mddp-license-mgmt-helm

- [mddp-license-mgmt-helm/.github/workflows/mddp-license-mgmt-helm.yml](mddp-license-mgmt-helm/.github/workflows/mddp-license-mgmt-helm.yml)
- [mddp-license-mgmt-helm/config.json](mddp-license-mgmt-helm/config.json)
- [mddp-license-mgmt-helm/jenkinsfile](mddp-license-mgmt-helm/jenkinsfile)

#### mddp-logging-helm

- [mddp-logging-helm/.github/workflows/mddp-logging-helm.yml](mddp-logging-helm/.github/workflows/mddp-logging-helm.yml)
- [mddp-logging-helm/config.json](mddp-logging-helm/config.json)
- [mddp-logging-helm/jenkinsfile](mddp-logging-helm/jenkinsfile)

#### mddp-messaging-helm

- [mddp-messaging-helm/.github/workflows/mddp-messaging-helm.yml](mddp-messaging-helm/.github/workflows/mddp-messaging-helm.yml)
- [mddp-messaging-helm/config.json](mddp-messaging-helm/config.json)
- [mddp-messaging-helm/jenkinsfile](mddp-messaging-helm/jenkinsfile)

#### mddp-messaging-kafka

- [mddp-messaging-kafka/.github/workflows/mddp-messaging-kafka.yml](mddp-messaging-kafka/.github/workflows/mddp-messaging-kafka.yml)
- [mddp-messaging-kafka/config.json](mddp-messaging-kafka/config.json)
- [mddp-messaging-kafka/jenkinsfile](mddp-messaging-kafka/jenkinsfile)

#### mddp-redis-caching

- [mddp-redis-caching/.github/workflows/mddp-redis-caching.yml](mddp-redis-caching/.github/workflows/mddp-redis-caching.yml)
- [mddp-redis-caching/config.json](mddp-redis-caching/config.json)
- [mddp-redis-caching/jenkinsfile](mddp-redis-caching/jenkinsfile)

#### mddp-secret-management

- [mddp-secret-management/.github/workflows/mddp-secret-management.yml](mddp-secret-management/.github/workflows/mddp-secret-management.yml)
- [mddp-secret-management/config.json](mddp-secret-management/config.json)
- [mddp-secret-management/jenkinsfile](mddp-secret-management/jenkinsfile)

#### mddp-secretmgmt-helm

- [mddp-secretmgmt-helm/.github/workflows/mddp-secretmgmt-helm.yml](mddp-secretmgmt-helm/.github/workflows/mddp-secretmgmt-helm.yml)
- [mddp-secretmgmt-helm/config.json](mddp-secretmgmt-helm/config.json)
- [mddp-secretmgmt-helm/jenkinsfile](mddp-secretmgmt-helm/jenkinsfile)

#### mddp-ui

- [mddp-ui/.github/workflows/mddp-ui.yml](mddp-ui/.github/workflows/mddp-ui.yml)
- [mddp-ui/config.json](mddp-ui/config.json)
- [mddp-ui/jenkinsfile](mddp-ui/jenkinsfile)

#### messaging-rabbitmq

- [messaging-rabbitmq/.github/workflows/messaging-rabbitmq.yml](messaging-rabbitmq/.github/workflows/messaging-rabbitmq.yml)
- [messaging-rabbitmq/config.json](messaging-rabbitmq/config.json)
- [messaging-rabbitmq/jenkinsfile](messaging-rabbitmq/jenkinsfile)

#### OPA-EC2

- [OPA-EC2/.github/workflows/opa-ec2.yml](OPA-EC2/.github/workflows/opa-ec2.yml)
- [OPA-EC2/config.json](OPA-EC2/config.json)
- [OPA-EC2/jenkinsfile](OPA-EC2/jenkinsfile)

#### OPA-region

- [OPA-region/.github/workflows/opa-region.yml](OPA-region/.github/workflows/opa-region.yml)
- [OPA-region/config.json](OPA-region/config.json)
- [OPA-region/jenkinsfile](OPA-region/jenkinsfile)

#### OPA-regions

- [OPA-regions/.github/workflows/opa-regions.yml](OPA-regions/.github/workflows/opa-regions.yml)
- [OPA-regions/config.json](OPA-regions/config.json)
- [OPA-regions/jenkinsfile](OPA-regions/jenkinsfile)

#### platform-dev-env

- [platform-dev-env/.github/workflows/platform-dev-env.yml](platform-dev-env/.github/workflows/platform-dev-env.yml)
- [platform-dev-env/config.json](platform-dev-env/config.json)
- [platform-dev-env/jenkinsfile](platform-dev-env/jenkinsfile)

#### platform-ui

- [platform-ui/.github/workflows/platform-ui.yml](platform-ui/.github/workflows/platform-ui.yml)
- [platform-ui/config.json](platform-ui/config.json)
- [platform-ui/jenkinsfile](platform-ui/jenkinsfile)

#### prechecks

- [prechecks/.github/workflows/prechecks.yml](prechecks/.github/workflows/prechecks.yml)
- [prechecks/config.json](prechecks/config.json)
- [prechecks/jenkinsfile](prechecks/jenkinsfile)

#### PrivateDockerConfig

- [PrivateDockerConfig/.github/workflows/privatedockerconfig.yml](PrivateDockerConfig/.github/workflows/privatedockerconfig.yml)
- [PrivateDockerConfig/config.json](PrivateDockerConfig/config.json)
- [PrivateDockerConfig/jenkinsfile](PrivateDockerConfig/jenkinsfile)

#### rayserve

- [rayserve/.github/workflows/rayserve.yml](rayserve/.github/workflows/rayserve.yml)
- [rayserve/config.json](rayserve/config.json)
- [rayserve/jenkinsfile](rayserve/jenkinsfile)

#### sampleAppDeploy

- [sampleAppDeploy/.github/workflows/sampleappdeploy.yml](sampleAppDeploy/.github/workflows/sampleappdeploy.yml)
- [sampleAppDeploy/config.json](sampleAppDeploy/config.json)
- [sampleAppDeploy/jenkinsfile](sampleAppDeploy/jenkinsfile)

#### sandbox-env

- [sandbox-env/.github/workflows/sandbox-env.yml](sandbox-env/.github/workflows/sandbox-env.yml)
- [sandbox-env/config.json](sandbox-env/config.json)
- [sandbox-env/jenkinsfile](sandbox-env/jenkinsfile)

#### skypilot

- [skypilot/.github/workflows/skypilot.yml](skypilot/.github/workflows/skypilot.yml)
- [skypilot/config.json](skypilot/config.json)
- [skypilot/jenkinsfile](skypilot/jenkinsfile)

#### sonarqube-test-ecocode

- [sonarqube-test-ecocode/.github/workflows/sonarqube-test-ecocode.yml](sonarqube-test-ecocode/.github/workflows/sonarqube-test-ecocode.yml)
- [sonarqube-test-ecocode/config.json](sonarqube-test-ecocode/config.json)
- [sonarqube-test-ecocode/jenkinsfile](sonarqube-test-ecocode/jenkinsfile)

#### sonartest

- [sonartest/.github/workflows/sonartest.yml](sonartest/.github/workflows/sonartest.yml)
- [sonartest/config.json](sonartest/config.json)
- [sonartest/jenkinsfile](sonartest/jenkinsfile)

#### Sourcery

- [Sourcery/.github/workflows/sourcery.yml](Sourcery/.github/workflows/sourcery.yml)
- [Sourcery/config.json](Sourcery/config.json)
- [Sourcery/jenkinsfile](Sourcery/jenkinsfile)

#### stress

- [stress/.github/workflows/stress.yml](stress/.github/workflows/stress.yml)
- [stress/config.json](stress/config.json)

#### Suggestions

- [Suggestions/.github/workflows/suggestions.yml](Suggestions/.github/workflows/suggestions.yml)
- [Suggestions/config.json](Suggestions/config.json)
- [Suggestions/jenkinsfile](Suggestions/jenkinsfile)

#### Sustainability_Automation

- [Sustainability_Automation/.github/workflows/sustainability_automation.yml](Sustainability_Automation/.github/workflows/sustainability_automation.yml)
- [Sustainability_Automation/config.json](Sustainability_Automation/config.json)
- [Sustainability_Automation/jenkinsfile](Sustainability_Automation/jenkinsfile)

#### Technology_Refreshment

- [Technology_Refreshment/.github/workflows/technology_refreshment.yml](Technology_Refreshment/.github/workflows/technology_refreshment.yml)
- [Technology_Refreshment/config.json](Technology_Refreshment/config.json)
- [Technology_Refreshment/jenkinsfile](Technology_Refreshment/jenkinsfile)

#### template-service

- [template-service/.github/workflows/template-service.yml](template-service/.github/workflows/template-service.yml)
- [template-service/config.json](template-service/config.json)
- [template-service/jenkinsfile](template-service/jenkinsfile)

#### Test_Pipeline

- [Test_Pipeline/.github/workflows/test_pipeline.yml](Test_Pipeline/.github/workflows/test_pipeline.yml)
- [Test_Pipeline/config.json](Test_Pipeline/config.json)
- [Test_Pipeline/jenkinsfile](Test_Pipeline/jenkinsfile)

#### TestEmail

- [TestEmail/.github/workflows/testemail.yml](TestEmail/.github/workflows/testemail.yml)
- [TestEmail/config.json](TestEmail/config.json)
- [TestEmail/jenkinsfile](TestEmail/jenkinsfile)

#### UninstallBigData

- [UninstallBigData/.github/workflows/uninstallbigdata.yml](UninstallBigData/.github/workflows/uninstallbigdata.yml)
- [UninstallBigData/config.json](UninstallBigData/config.json)
- [UninstallBigData/jenkinsfile](UninstallBigData/jenkinsfile)

#### vuln-scanning

- [vuln-scanning/.github/workflows/vuln-scanning.yml](vuln-scanning/.github/workflows/vuln-scanning.yml)
- [vuln-scanning/config.json](vuln-scanning/config.json)
- [vuln-scanning/jenkinsfile](vuln-scanning/jenkinsfile)

### Partially successful

#### Add_worker_to_K8s

- [Add_worker_to_K8s/.github/workflows/add_worker_to_k8s.yml](Add_worker_to_K8s/.github/workflows/add_worker_to_k8s.yml)
- [Add_worker_to_K8s/config.json](Add_worker_to_K8s/config.json)
- [Add_worker_to_K8s/jenkinsfile](Add_worker_to_K8s/jenkinsfile)

#### auto-healing

- [auto-healing/.github/workflows/auto-healing.yml](auto-healing/.github/workflows/auto-healing.yml)
- [auto-healing/config.json](auto-healing/config.json)
- [auto-healing/jenkinsfile](auto-healing/jenkinsfile)

#### auto-remediation-ansible

- [auto-remediation-ansible/.github/workflows/auto-remediation-ansible.yml](auto-remediation-ansible/.github/workflows/auto-remediation-ansible.yml)
- [auto-remediation-ansible/config.json](auto-remediation-ansible/config.json)
- [auto-remediation-ansible/jenkinsfile](auto-remediation-ansible/jenkinsfile)

#### awx-parallel

- [awx-parallel/.github/workflows/awx-parallel.yml](awx-parallel/.github/workflows/awx-parallel.yml)
- [awx-parallel/config.json](awx-parallel/config.json)
- [awx-parallel/jenkinsfile](awx-parallel/jenkinsfile)

#### awx_single

- [awx_single/.github/workflows/awx_single.yml](awx_single/.github/workflows/awx_single.yml)
- [awx_single/config.json](awx_single/config.json)
- [awx_single/jenkinsfile](awx_single/jenkinsfile)

#### breakingPointK6

- [breakingPointK6/.github/workflows/breakingpointk6.yml](breakingPointK6/.github/workflows/breakingpointk6.yml)
- [breakingPointK6/config.json](breakingPointK6/config.json)
- [breakingPointK6/jenkinsfile](breakingPointK6/jenkinsfile)

#### breakingPointLocust

- [breakingPointLocust/.github/workflows/breakingpointlocust.yml](breakingPointLocust/.github/workflows/breakingpointlocust.yml)
- [breakingPointLocust/config.json](breakingPointLocust/config.json)
- [breakingPointLocust/jenkinsfile](breakingPointLocust/jenkinsfile)

#### chaosTestK6

- [chaosTestK6/.github/workflows/chaostestk6.yml](chaosTestK6/.github/workflows/chaostestk6.yml)
- [chaosTestK6/config.json](chaosTestK6/config.json)
- [chaosTestK6/jenkinsfile](chaosTestK6/jenkinsfile)

#### chaosTestLocust

- [chaosTestLocust/.github/workflows/chaostestlocust.yml](chaosTestLocust/.github/workflows/chaostestlocust.yml)
- [chaosTestLocust/config.json](chaosTestLocust/config.json)
- [chaosTestLocust/jenkinsfile](chaosTestLocust/jenkinsfile)

#### chaosTestLocustOldImp

- [chaosTestLocustOldImp/.github/workflows/chaostestlocustoldimp.yml](chaosTestLocustOldImp/.github/workflows/chaostestlocustoldimp.yml)
- [chaosTestLocustOldImp/config.json](chaosTestLocustOldImp/config.json)
- [chaosTestLocustOldImp/jenkinsfile](chaosTestLocustOldImp/jenkinsfile)

#### check

- [check/.github/workflows/check.yml](check/.github/workflows/check.yml)
- [check/config.json](check/config.json)
- [check/jenkinsfile](check/jenkinsfile)

#### Cluster

- [Cluster/.github/workflows/cluster.yml](Cluster/.github/workflows/cluster.yml)
- [Cluster/config.json](Cluster/config.json)
- [Cluster/jenkinsfile](Cluster/jenkinsfile)

#### cluster_microservices

- [cluster_microservices/.github/workflows/cluster_microservices.yml](cluster_microservices/.github/workflows/cluster_microservices.yml)
- [cluster_microservices/config.json](cluster_microservices/config.json)
- [cluster_microservices/jenkinsfile](cluster_microservices/jenkinsfile)

#### clusterms

- [clusterms/.github/workflows/clusterms.yml](clusterms/.github/workflows/clusterms.yml)
- [clusterms/config.json](clusterms/config.json)
- [clusterms/jenkinsfile](clusterms/jenkinsfile)

#### criticalServiceList

- [criticalServiceList/.github/workflows/criticalservicelist.yml](criticalServiceList/.github/workflows/criticalservicelist.yml)
- [criticalServiceList/config.json](criticalServiceList/config.json)
- [criticalServiceList/jenkinsfile](criticalServiceList/jenkinsfile)

#### Deploy_Pipeline

- [Deploy_Pipeline/.github/workflows/deploy_pipeline.yml](Deploy_Pipeline/.github/workflows/deploy_pipeline.yml)
- [Deploy_Pipeline/config.json](Deploy_Pipeline/config.json)
- [Deploy_Pipeline/jenkinsfile](Deploy_Pipeline/jenkinsfile)

#### Destroy

- [Destroy/.github/workflows/destroy.yml](Destroy/.github/workflows/destroy.yml)
- [Destroy/config.json](Destroy/config.json)
- [Destroy/jenkinsfile](Destroy/jenkinsfile)

#### development

- [development/.github/workflows/development.yml](development/.github/workflows/development.yml)
- [development/config.json](development/config.json)
- [development/jenkinsfile](development/jenkinsfile)

#### DockerImage_Scan

- [DockerImage_Scan/.github/workflows/dockerimage_scan.yml](DockerImage_Scan/.github/workflows/dockerimage_scan.yml)
- [DockerImage_Scan/config.json](DockerImage_Scan/config.json)
- [DockerImage_Scan/jenkinsfile](DockerImage_Scan/jenkinsfile)

#### ecocode-for-python

- [ecocode-for-python/.github/workflows/ecocode-for-python.yml](ecocode-for-python/.github/workflows/ecocode-for-python.yml)
- [ecocode-for-python/config.json](ecocode-for-python/config.json)
- [ecocode-for-python/jenkinsfile](ecocode-for-python/jenkinsfile)

#### ecocode-python

- [ecocode-python/.github/workflows/ecocode-python.yml](ecocode-python/.github/workflows/ecocode-python.yml)
- [ecocode-python/config.json](ecocode-python/config.json)
- [ecocode-python/jenkinsfile](ecocode-python/jenkinsfile)

#### GenAI_Deployment

- [GenAI_Deployment/.github/workflows/genai_deployment.yml](GenAI_Deployment/.github/workflows/genai_deployment.yml)
- [GenAI_Deployment/config.json](GenAI_Deployment/config.json)
- [GenAI_Deployment/jenkinsfile](GenAI_Deployment/jenkinsfile)

#### Jenkins_Jira_Integration

- [Jenkins_Jira_Integration/.github/workflows/jenkins_jira_integration.yml](Jenkins_Jira_Integration/.github/workflows/jenkins_jira_integration.yml)
- [Jenkins_Jira_Integration/config.json](Jenkins_Jira_Integration/config.json)
- [Jenkins_Jira_Integration/jenkinsfile](Jenkins_Jira_Integration/jenkinsfile)

#### kor

- [kor/.github/workflows/kor.yml](kor/.github/workflows/kor.yml)
- [kor/config.json](kor/config.json)
- [kor/jenkinsfile](kor/jenkinsfile)

#### ngnix

- [ngnix/.github/workflows/ngnix.yml](ngnix/.github/workflows/ngnix.yml)
- [ngnix/config.json](ngnix/config.json)
- [ngnix/jenkinsfile](ngnix/jenkinsfile)

#### Palto_Alto

- [Palto_Alto/.github/workflows/palto_alto.yml](Palto_Alto/.github/workflows/palto_alto.yml)
- [Palto_Alto/config.json](Palto_Alto/config.json)
- [Palto_Alto/jenkinsfile](Palto_Alto/jenkinsfile)

#### parallelTest

- [parallelTest/.github/workflows/paralleltest.yml](parallelTest/.github/workflows/paralleltest.yml)
- [parallelTest/config.json](parallelTest/config.json)
- [parallelTest/jenkinsfile](parallelTest/jenkinsfile)

#### s3-policies

- [s3-policies/.github/workflows/s3-policies.yml](s3-policies/.github/workflows/s3-policies.yml)
- [s3-policies/config.json](s3-policies/config.json)
- [s3-policies/jenkinsfile](s3-policies/jenkinsfile)

#### sample

- [sample/.github/workflows/sample.yml](sample/.github/workflows/sample.yml)
- [sample/config.json](sample/config.json)
- [sample/jenkinsfile](sample/jenkinsfile)

#### testCluster

- [testCluster/.github/workflows/testcluster.yml](testCluster/.github/workflows/testcluster.yml)
- [testCluster/config.json](testCluster/config.json)
- [testCluster/jenkinsfile](testCluster/jenkinsfile)

#### Tools_create_db_container

- [Tools_create_db_container/.github/workflows/tools_create_db_container.yml](Tools_create_db_container/.github/workflows/tools_create_db_container.yml)
- [Tools_create_db_container/config.json](Tools_create_db_container/config.json)
- [Tools_create_db_container/jenkinsfile](Tools_create_db_container/jenkinsfile)

#### Tools_create_permission_container

- [Tools_create_permission_container/.github/workflows/tools_create_permission_container.yml](Tools_create_permission_container/.github/workflows/tools_create_permission_container.yml)
- [Tools_create_permission_container/config.json](Tools_create_permission_container/config.json)
- [Tools_create_permission_container/jenkinsfile](Tools_create_permission_container/jenkinsfile)

#### Tools_create_user_container

- [Tools_create_user_container/.github/workflows/tools_create_user_container.yml](Tools_create_user_container/.github/workflows/tools_create_user_container.yml)
- [Tools_create_user_container/config.json](Tools_create_user_container/config.json)
- [Tools_create_user_container/jenkinsfile](Tools_create_user_container/jenkinsfile)

#### Tools_deletion_container

- [Tools_deletion_container/.github/workflows/tools_deletion_container.yml](Tools_deletion_container/.github/workflows/tools_deletion_container.yml)
- [Tools_deletion_container/config.json](Tools_deletion_container/config.json)
- [Tools_deletion_container/jenkinsfile](Tools_deletion_container/jenkinsfile)

#### Tools_Deployment

- [Tools_Deployment/.github/workflows/tools_deployment.yml](Tools_Deployment/.github/workflows/tools_deployment.yml)
- [Tools_Deployment/config.json](Tools_Deployment/config.json)
- [Tools_Deployment/jenkinsfile](Tools_Deployment/jenkinsfile)

#### Tools_installation

- [Tools_installation/.github/workflows/tools_installation.yml](Tools_installation/.github/workflows/tools_installation.yml)
- [Tools_installation/config.json](Tools_installation/config.json)
- [Tools_installation/jenkinsfile](Tools_installation/jenkinsfile)

#### Tools_intallation_container

- [Tools_intallation_container/.github/workflows/tools_intallation_container.yml](Tools_intallation_container/.github/workflows/tools_intallation_container.yml)
- [Tools_intallation_container/config.json](Tools_intallation_container/config.json)
- [Tools_intallation_container/jenkinsfile](Tools_intallation_container/jenkinsfile)

### Failed

#### AI-Automated-Pipeline

- [AI-Automated-Pipeline/error.txt](AI-Automated-Pipeline/error.txt)
- [AI-Automated-Pipeline/config.json](AI-Automated-Pipeline/config.json)

#### GenAI_POC_AutoBuild

- [GenAI_POC_AutoBuild/error.txt](GenAI_POC_AutoBuild/error.txt)
- [GenAI_POC_AutoBuild/config.json](GenAI_POC_AutoBuild/config.json)

#### Intel_V2

- [Intel_V2/error.txt](Intel_V2/error.txt)
- [Intel_V2/config.json](Intel_V2/config.json)

#### sustain

- [sustain/error.txt](sustain/error.txt)
- [sustain/config.json](sustain/config.json)

#### Sustainable_workload_benchamrking

- [Sustainable_workload_benchamrking/error.txt](Sustainable_workload_benchamrking/error.txt)
- [Sustainable_workload_benchamrking/config.json](Sustainable_workload_benchamrking/config.json)

#### WorkLoad_Benchmarking

- [WorkLoad_Benchmarking/error.txt](WorkLoad_Benchmarking/error.txt)
- [WorkLoad_Benchmarking/config.json](WorkLoad_Benchmarking/config.json)