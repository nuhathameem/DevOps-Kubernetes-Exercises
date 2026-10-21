# Exercise 1: Kubernetes Getting Started (Hello Pod)

## Objective

Deploy a web application (Nginx, simulating Zepto's storefront) as a Pod on a local Kubernetes cluster using Minikube, and access it from the browser.

## Business Problem (Zepto Example)

Imagine you are a DevOps Engineer at Zepto. The product team has built a lightweight web application that displays the storefront and delivery status page for customers.

Your task is to deploy this application on Kubernetes so that it is always running, portable, and can be scaled later. This is simulated using the Nginx container image.

## Environment

- Windows 11
- Docker Desktop
- Minikube with Docker driver
- Kubernetes CLI (`kubectl`)
- Microsoft PowerShell
- Nginx container image

## Steps and Commands

### 1. Start the Kubernetes Cluster

Start the local Kubernetes cluster using Minikube.

```powershell
minikube start --driver=docker
```

### 2. Create a Pod Using the Nginx Image

Create a Kubernetes Pod named `hello-k8s` using the Nginx image.

```powershell
kubectl run hello-k8s --image=nginx --port=80
```

### 3. Verify the Pod Is Running

Check the status of the Pod.

```powershell
kubectl get pods
```

Wait until the Pod shows `1/1` under READY and `Running` under STATUS.

### 4. Expose the Pod as a NodePort Service

Expose the application so that it can be accessed from outside the cluster.

```powershell
kubectl expose pod hello-k8s --type=NodePort --port=80
```

### 5. Verify the Kubernetes Service

Check whether the service has been created successfully.

```powershell
kubectl get services
```

### 6. Access the Application in the Browser

Run the following command to open the application.

```powershell
minikube service hello-k8s
```

Minikube provides a local URL and opens the application in the browser. Keep the PowerShell terminal open while the service tunnel is running.

The Nginx welcome page confirms that the application is running successfully.

## Output Screenshots

### 1. Nginx Welcome Page in Browser

![Kubernetes Pod and Service](screenshots/Screenshot%202026-10-21%20183615.png)

### 2. Kubernetes Pod and Service

![Nginx Welcome Page](screenshots/Screenshot%202026-10-21%20190506.png)

## Result

Successfully created and verified a Kubernetes Pod running Nginx, exposed it through a NodePort service, and accessed the application through a web browser using Minikube.

## Conclusion

This exercise demonstrates the basic Kubernetes workflow of starting a local cluster, deploying a containerized application, verifying the Pod, exposing the application through a service, and accessing it from a browser.
