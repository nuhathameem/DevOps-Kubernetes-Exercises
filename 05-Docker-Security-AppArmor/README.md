# Docker Security with AppArmor and Python

## Objective
Secure a Dockerized Flask application using an AppArmor profile and the Docker SDK for Python.

## Files
- `app.py` - Flask web application.
- `Dockerfile` - Docker image configuration.
- `requirements.txt` - Python dependencies.
- `my-apparmor-profile` - Requested AppArmor profile.
- `apply_apparmor.py` - Builds the image, requests the AppArmor security option, and inspects the container configuration.
- `test_restricted_actions.py` - Tests reading `/etc/passwd` and executing `/bin/bash`.
- `screenshots/` - Evidence screenshots.

## Execution and Results

1. Built the Docker image `flask-apparmor`.
2. Started the Flask container and verified the response at `http://localhost:5000`.
3. Ran the Docker SDK script. Docker reported the configured option `apparmor=my-apparmor-profile`.
4. Tested restricted actions. Reading `/etc/passwd` returned exit code 0, and executing `/bin/bash` also returned exit code 0.
5. Removed the temporary test container after testing.

## Environment Limitation

Docker Desktop did not list AppArmor among the security options reported by `docker info`. Although the Docker SDK inspection reported the requested AppArmor option, the restricted-action tests succeeded. Therefore, AppArmor enforcement was not demonstrated in this environment, and the tests do not prove that the intended restrictions were enforced.

## Theory Questions and Answers

### 1. What is the purpose of using AppArmor with Docker containers?
AppArmor enforces security policies and confines applications to a limited set of resources. With Docker containers, it can limit access to system resources, files, and networks, adding another layer of security.

### 2. How do AppArmor profiles help secure a Docker container?
AppArmor profiles define what a containerized application can and cannot do. They can restrict access to sensitive directories, network capabilities, file execution, and system calls.

### 3. Why is it important to restrict access to sensitive directories such as `/etc/` and `/var/`?
The `/etc/` directory contains configuration files and system settings. Restricting access helps prevent unauthorized reading or modification of important files and reduces security risks.

### 4. What other capabilities can you restrict using AppArmor profiles?
AppArmor profiles can restrict network access, port binding, binary execution, writing to specific directories, and system-administration capabilities such as `cap_sys_admin`.

### 5. How can you verify if an AppArmor profile is successfully applied to a Docker container?
The Docker CLI or Docker SDK can be used to inspect the container's security options. The `HostConfig.SecurityOpt` field shows configured options, but kernel-level enforcement should also be verified separately.
