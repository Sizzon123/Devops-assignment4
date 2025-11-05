# 🚀 Flask App Deployment with Docker & GitHub Actions

This project demonstrates how to containerize a Python Flask application, manage environment variables securely, automate builds using GitHub Actions, and implement Dependabot for dependency updates.

---

## 📌 Features

- Flask app with two routes:
  - `/` displays a message from `APP_MESSAGE`
  - `/health` displays a status from `APP_HEALTH`
- Dockerized using `Dockerfile` and `docker-compose.yml`
- Environment variables managed via `.env` and GitHub Secrets
- CI/CD pipeline using GitHub Actions
- Weekly dependency updates via Dependabot

---

## 🧱 Project Structure

```bash
├── app.py 
├── requirements.txt 
├── Dockerfile 
├── docker-compose.yml 
├── .env # Not committed 
├── .env.example # Sample values for testing 
├── .gitignore 
├── templates/ 
│ ├── home.html 
│ └── health.html 
└── .github/ 
  └── workflows/ 
     └── ci.yml
```

---

## 🧪 Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/Sizzon123/Devops-assignment4.git
cd Devops-assignment4.git
docker compose up --build
```
