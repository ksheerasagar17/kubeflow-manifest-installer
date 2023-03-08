import os
import subprocess
import time

# Set the working directory to where the kustomization.yaml file is located
os.chdir("manifest\manifests-1.6.1\example")

# Deploy the Kubeflow application
subprocess.run("kustomize build example | kubectl delete -k -", shell=True)


# Check the deployment status in a while loop
uninstall_successful = False
while not uninstall_successful:
    # Get the deployment status
    output = subprocess.check_output(
        "kubectl get pods -n kubeflow", shell=True)
    lines = output.decode().split("\n")
    # Check if all deployments are ready
    ready_deployments = [
        line for line in lines if "Terminating" in line or "Completed" in line]
    if len(ready_deployments) == len(lines) - 1:
        time.sleep(10)
    else:
        # Wait for 10 seconds before checking again
        uninstall_successful = True

# kubectl get pods -n kubeflow
# kubectl get svc -n kubeflow

# kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
# http://localhost:8080
# kubectl get crd | grep kubeflow

# Print a message to indicate successful installation
print("Kubeflow uninstall successful!")
