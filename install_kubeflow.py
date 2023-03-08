import os
import subprocess
import time
# from kustomize import pykustomize

# Set the working directory to where the kustomization.yaml file is located
os.chdir("manifest\manifests-1.6.1")

# Deploy the Kubeflow application
subprocess.run("kustomize build example | kubectl apply -f -", shell=True)

# Check the deployment status in a while loop
deployment_successful = False
while not deployment_successful:
    # Get the deployment status
    output = subprocess.check_output(
        "kubectl get pods -n kubeflow", shell=True)
    lines = output.decode().split("\n")
    # Check if all deployments are ready
    ready_deployments = [
        line for line in lines if "Running" in line or "Completed" in line]
    if len(ready_deployments) == len(lines) - 1:
        deployment_successful = True
    else:
        # Wait for 10 seconds before checking again
        time.sleep(10)

# kubectl get pods -n kubeflow
# kubectl get svc -n kubeflow

# kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
# http://localhost:8080
# kubectl get crd | grep kubeflow

# Print a message to indicate successful installation
print("Kubeflow installation successful!")
