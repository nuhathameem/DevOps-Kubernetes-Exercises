# Exercise 2: Minikube, Kubectl and Flask Deployment

## Objective

Build a Docker image for a Flask application, load it into Minikube, deploy it as a Kubernetes Pod, expose it using a NodePort Service, and access it through a web browser.

## Business Problem

A development team needs to deploy a lightweight Python Flask application on a local Kubernetes cluster. The application must run inside a container, be managed by Kubernetes, and be accessible through a browser.

## Technologies Used

- Docker Desktop
- Minikube
- Kubernetes
- kubectl
- Python
- Flask
- Windows PowerShell

## Implementation Steps

### 1. Create the Flask Application

Created `app.py` containing a Flask application that returns the message:

`Hello from Flask on Kubernetes!`

Created the following project files:

- `app.py`
- `Dockerfile`
- `requirements.txt`

### 2. Build the Docker Image

Built the Docker image using:

```powershell
docker build -t flask-k8s-app:latest .
```

The Docker image was built successfully.

### 3. Verify the Docker Image

Verified the image using:

```powershell
docker images flask-k8s-app
```

The image `flask-k8s-app:latest` was available locally.

### 4. Verify Minikube

Checked the Minikube cluster status:

```powershell
minikube status
```

The host, kubelet, and API server were running, and kubeconfig was configured.

### 5. Load the Docker Image into Minikube

Loaded the image into Minikube:

```powershell
minikube image load flask-k8s-app:latest
```

Verified the available images using:

```powershell
minikube image ls
```

The Flask image was present in the image list.

### 6. Deploy the Flask Application

Created a Kubernetes Pod:

```powershell
kubectl run flask-app --image=flask-k8s-app:latest --image-pull-policy=Never --port=15000
```

Verified the Pod status:

```powershell
kubectl get pods
```

The `flask-app` Pod reached the `Running` state with `1/1` containers ready.

### 7. Expose the Application

Created a NodePort Service:

```powershell
kubectl expose pod flask-app --type=NodePort --port=15000
```

Verified the Service:

```powershell
kubectl get services
```

The `flask-app` Service was created with NodePort `31817`.

### 8. Access the Application

Opened the application using:

```powershell
minikube service flask-app
```

The application was successfully accessed through the browser.

## Output Screenshots

Screenshots will be stored in the `screenshots/` directory.

### 1. Flask Application Files

![Flask application files](screenshots/flask-app-files.png)

### 2. Docker Image Build

![Docker image build](screenshots/docker-image-build.png)

### 3. Docker Image Verification

![Docker image verification](screenshots/docker-image-verification.png)

### 4. Minikube Image Loaded

![Minikube image loaded](screenshots/minikube-image-loaded.png)

### 5. Flask Pod Running

![Flask Pod running](screenshots/flask-pod-running.png)

### 6. Flask NodePort Service

![Flask Service](screenshots/flask-service.png)

### 7. Flask Application in Browser

![Flask browser output](screenshots/flask-browser-output.png)

## Result

Successfully built a Docker image for a Flask application, loaded it into Minikube, deployed it as a Kubernetes Pod, exposed it through a NodePort Service, and verified the application in a browser.
