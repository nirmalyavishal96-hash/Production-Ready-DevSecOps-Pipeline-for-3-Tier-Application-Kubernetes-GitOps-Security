#  DevSecOps 3-Tier Application (Flask + Kubernetes + GitOps)

![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployment-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)
![ArgoCD](https://img.shields.io/badge/ArgoCD-GitOps-orange)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-yellow)
![Grafana](https://img.shields.io/badge/Visualization-Grafana-orange)
![Trivy](https://img.shields.io/badge/Security-Trivy-green)

---

## 📌 Problem Statement

Modern applications require **secure, automated, and reliable deployment pipelines**, but many systems lack:

- Automated vulnerability scanning  
- Continuous deployment with rollback capability  
- Real-time monitoring and alerting  
- Standardized and repeatable infrastructure  

---

## 💡 Solution

This project implements a **production-style DevSecOps pipeline** that:

- Automates build, scan, and deployment workflows  
- Ensures only secure container images are deployed  
- Uses **GitOps (ArgoCD)** for consistent and auditable deployments  
- Provides real-time monitoring using **Prometheus & Grafana**  
- Triggers alerts using **Alertmanager (Email notifications)**  

---

## 📈 Impact

- Reduced manual deployment effort by ~80% through CI/CD automation  
- Improved deployment reliability using GitOps-based synchronization  
- Prevented vulnerable images from reaching production using Trivy scanning  
- Enabled faster incident response with real-time monitoring and alerts  

---

## 🏗️ Architecture

```
User
  ↓
Nginx (Reverse Proxy)
  ↓
Flask Application (API + Metrics)
  ↓
PostgreSQL Database

Monitoring Stack:
Flask → Prometheus → Alertmanager → Email
                   ↓
                Grafana
```

---

## ⚙️ Tech Stack

| Category         | Tools Used                |
| ---------------- | ------------------------- |
| Backend          | Flask (Python)            |
| Database         | PostgreSQL                |
| Containerization | Docker, Docker Compose    |
| Orchestration    | Kubernetes (Minikube)     |
| Package Manager  | Helm                      |
| GitOps           | ArgoCD                    |
| Monitoring       | Prometheus                |
| Visualization    | Grafana                   |
| Alerting         | Alertmanager (Gmail SMTP) |
| CI/CD            | Jenkins                   |
| Security Scanning| Trivy                     |

---

## 🔐 Security (DevSecOps)

### 🔍 Trivy Image Scanning

Integrated **Trivy** in the CI/CD pipeline to scan Docker images for vulnerabilities.

* Scans for:

  * OS package vulnerabilities
  * Application dependencies
  * Misconfigurations

* Ensures only secure images are deployed to Kubernetes
---
### 🔁 Security Workflow

1. Jenkins builds Docker image
2. Trivy scans the image
3. If vulnerabilities found → build can be failed (configurable)
4. Secure image pushed to DockerHub
5. ArgoCD deploys only validated images

### 📌 Example Command

```bash
trivy image nirmalyavishal97/devsecops-flask-app:latest
```
---

## 🔁 DevOps Workflow

1. Developer pushes code to GitHub
2. Jenkins builds Docker image & pushes to DockerHub
3. Helm chart updated with new image tag
4. ArgoCD syncs Kubernetes cluster automatically
5. Application deployed to Kubernetes
6. Prometheus scrapes metrics
7. Alerts triggered via Alertmanager
8. Notifications sent via Email

---


## 🔄 GitOps (ArgoCD)

* Continuous deployment using ArgoCD
* Auto-sync enabled from GitHub repo
* Declarative Kubernetes deployments using Helm

---

## 📊 Monitoring & Alerting

### 🔹 Prometheus

* Scrapes custom metrics from Flask (`/metrics`)
* Tracks request count & CPU usage

### 🔹 Grafana

* Visual dashboards for:

  * CPU usage
  * Request metrics
  * Application health

### 🔹 Alertmanager

* Email alerts configured via Gmail SMTP
* Example alert:

  * **HighCPUUsage (>70%)**

---

## 📸 Screenshots

### 🖥️ Application UI

![App UI](screenshots/Application-UI.png)

### 🔄 ArgoCD Sync

![ArgoCD](screenshots/ArgoCD-sync.png)

### 📊 Grafana Dashboard

![Grafana](screenshots/Grafana-Dashboard.png)

### 🚨 Prometheus Alert Firing

![Prometheus](screenshots/Prometheus_Target_Firing.png)

### 📧 Email Alert

![Email](screenshots/Email-alert.png)

### ⚙️ Jenkins Pipeline

![Jenkins](screenshots/Jenkins-pipeline.png)

---

## 🛠️ Setup Instructions

### 🔹 Clone Repo

```bash
git clone https://github.com/nirmalyavishal96-hash/Production-Ready-DevSecOps-Pipeline-for-3-Tier-Application-Kubernetes-GitOps-Security.git
cd Production-Ready-DevSecOps-Pipeline-for-3-Tier-Application-Kubernetes-GitOps-Security
```

---

### 🔹 Run Locally (Docker Compose)

```bash
docker-compose up --build
```

---

### 🔹 Kubernetes Deployment

```bash
# Apply Kubernetes manifests
kubectl apply -f kubernetes/

# OR using Helm
helm install flask-app ./helm/flask-app
```

---

### 🔹 Database Setup (Important)

```bash
export FLASK_APP=run.py

flask db init
flask db migrate -m "initial"
flask db upgrade
```

---

## 🔐 Security Considerations

* Environment variables used for secrets
* No hardcoded credentials in code
* JWT-based authentication implemented
* Ready for integration with:

  * Kubernetes Secrets
  * Vault (future enhancement)

---

## 🚀 Key Features

* 🔐 JWT Authentication
* 📋 Task Management API
* 📊 Custom Metrics Export (/metrics)
* 📦 Helm-based Deployment
* 🔄 GitOps with ArgoCD
* 📈 Monitoring & Alerting
* ⚙️ CI/CD Pipeline with Jenkins

---

## 🔮 Future Improvements

* Add HPA (Horizontal Pod Autoscaling)
* Integrate Kubernetes Secrets
* Add Ingress Controller (NGINX)
* Implement RBAC & Network Policies
* Add Tracing (Jaeger)
* Move to cloud (AWS / Azure)

---

## 👨‍💻 Author

**Nirmalya Das**
DevOps Engineer | Cloud | Kubernetes | CI/CD

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and connect with me on LinkedIn!

---

