# 🚀 DevSecOps 3-Tier Application on Kubernetes

![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployment-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)
![ArgoCD](https://img.shields.io/badge/ArgoCD-GitOps-orange)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-yellow)
![Grafana](https://img.shields.io/badge/Visualization-Grafana-orange)
![Trivy](https://img.shields.io/badge/Security-Trivy-green)

---

## 📌 Project Overview

A **production-grade DevSecOps 3-tier application** deployed on Kubernetes using modern DevOps practices:

* CI/CD with Jenkins
* GitOps with ArgoCD
* Container security with Trivy
* Monitoring with Prometheus & Grafana
* Alerting with Alertmanager

---

## 🏗️ Architecture

```
Frontend (Nginx)
        ↓
Backend (Flask API)
        ↓
Database (PostgreSQL)
```

---

## ⚙️ Tech Stack

| Layer         | Tools                 |
| ------------- | --------------------- |
| Frontend      | Nginx                 |
| Backend       | Flask                 |
| Database      | PostgreSQL            |
| Container     | Docker                |
| Orchestration | Kubernetes (Minikube) |
| CI/CD         | Jenkins               |
| GitOps        | ArgoCD                |
| Monitoring    | Prometheus            |
| Visualization | Grafana               |
| Security      | Trivy                 |
| Alerting      | Alertmanager          |

---

## 🚀 Features

* End-to-end CI/CD pipeline
* GitOps-based deployment
* Real-time monitoring & alerts
* Secure container scanning
* Scalable Kubernetes deployment

---

## 📸 Screenshots

Attached:

* Jenkins Pipeline Success
* ArgoCD Sync Status
* Grafana Dashboard
* Prometheus Targets
* Alertmanager Email
* Application UI

---

## 🛠️ Setup Instructions

### 1. Start Minikube

```bash
minikube start
```

### 2. Deploy Database

```bash
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/postgres-service.yaml
```

### 3. Deploy Backend

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 4. Deploy Frontend

```bash
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml
```

---

## 🔍 Troubleshooting

| Issue                         | Solution           |
| ----------------------------- | ------------------ |
| CrashLoopBackOff              | Fix Docker CMD     |
| Git push failed               | Use rebase         |
| Service not accessible        | Check port-forward |
| Frontend cannot reach backend | Use Nginx proxy    |
| Minikube browser error        | Use manual URL     |

---

## 🔐 Security

* Integrated Trivy for vulnerability scanning
* Secure CI pipeline

---

## 📊 Monitoring

* Prometheus scraping metrics
* Grafana dashboards
* Alertmanager email alerts

---

## 🎯 Outcome

This project demonstrates:

* Real-world DevSecOps pipeline
* Kubernetes production deployment
* Observability and security integration

---

## 👨‍💻 Author

**Nirmalya Das**
