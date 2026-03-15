# Kubernetes Autoscaling POC with Flask

## Overview

This project demonstrates how Kubernetes autoscaling mechanisms work
using a simple Python Flask application.\
The application exposes multiple endpoints that intentionally generate
CPU, memory, or long-running workloads so that Kubernetes autoscaling
features can be observed in action.

This POC demonstrates:

-   Horizontal Pod Autoscaler (HPA)
-   Vertical Pod Autoscaler (VPA)
-   Cluster Autoscaler

The project is designed for DevOps / MLOps learning and works well for
demonstrations on GKE or any Kubernetes cluster.

------------------------------------------------------------------------

# Architecture

User Browser → Flask Frontend → Flask Backend Endpoints → CPU / Memory
Load\
→ Kubernetes Metrics Server → HPA / VPA → Cluster Autoscaler

Autoscaling Flow:

1.  User triggers load from the frontend UI.
2.  Flask endpoint creates CPU or memory pressure.
3.  Kubernetes metrics server detects resource usage.
4.  HPA scales pods based on CPU utilization.
5.  VPA adjusts resource requests if enabled.
6.  If pods cannot be scheduled due to insufficient nodes, Cluster
    Autoscaler adds nodes.

------------------------------------------------------------------------

# Project Structure

autoscaler-poc/

backend/ app.py

frontend/ index.html

requirements.txt

Dockerfile

k8s/ deployment.yaml service.yaml hpa.yaml vpa.yaml

------------------------------------------------------------------------

# Flask Endpoints

/\
Frontend UI to trigger tests

/health\
Basic health check

/cpu-load\
Generates heavy CPU usage to trigger Horizontal Pod Autoscaler

/memory-load\
Allocates large memory to demonstrate Vertical Pod Autoscaler
adjustments

/long-request\
Simulates long-running requests

------------------------------------------------------------------------

# Running Locally

Install dependencies

pip install -r requirements.txt

Run Flask app

python backend/app.py

Open browser

http://localhost:5000

------------------------------------------------------------------------

# Build Docker Image

docker build -t autoscaler-demo .

Push image to container registry

docker tag autoscaler-demo
`<your-dockerhub-username>`{=html}/autoscaler-demo

docker push `<your-dockerhub-username>`{=html}/autoscaler-demo

------------------------------------------------------------------------

# Kubernetes Deployment

Apply manifests

kubectl apply -f k8s/

Verify pods

kubectl get pods

Verify service

kubectl get svc

------------------------------------------------------------------------

# Horizontal Pod Autoscaler

Check HPA status

kubectl get hpa

Watch scaling

kubectl get hpa -w

Trigger CPU load from UI or using load testing

Example using hey

hey -z 60s http://`<EXTERNAL-IP>`{=html}/cpu-load

Pods should scale automatically based on CPU utilization.

------------------------------------------------------------------------

# Vertical Pod Autoscaler

Install VPA components in cluster if not already installed.

Apply VPA manifest

kubectl apply -f k8s/vpa.yaml

Check recommendations

kubectl describe vpa

VPA will recommend or automatically update container resource requests.

------------------------------------------------------------------------

# Cluster Autoscaler

Cluster autoscaler automatically adds nodes when:

-   Pods are pending
-   Cluster does not have enough capacity

Steps to demonstrate:

1.  Increase HPA max replicas
2.  Generate heavy traffic
3.  Pods become pending
4.  Cluster Autoscaler provisions new nodes

Verify nodes

kubectl get nodes

------------------------------------------------------------------------

# Monitoring Autoscaling

Useful commands

kubectl top pods kubectl top nodes kubectl describe hpa kubectl describe
vpa

------------------------------------------------------------------------

# Learning Outcomes

After running this POC you will understand:

-   How HPA uses CPU metrics
-   Why resource requests are required
-   How VPA recommends CPU and memory
-   How cluster autoscaler adds nodes when pods cannot schedule

------------------------------------------------------------------------

# Use Case for DevOps Portfolio

This project demonstrates hands-on knowledge of:

-   Kubernetes autoscaling
-   Flask application containerization
-   Docker
-   Kubernetes deployments and services
-   Observing scaling behavior in real environments

This type of project is useful for DevOps, Cloud Engineer, and MLOps
interviews.
