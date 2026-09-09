# Inventory Management API 📦

An asynchronous RESTful API for inventory management and stock control, built with **FastAPI**, **SQLAlchemy (Async)**, **Alembic**, and **PostgreSQL**. The project is containerized using **Docker** and deployed to the cloud via **Render**.

🌐 **Languages:** [English](#english) | [Español](#espanol)

---

<div id="english"></div>

## 🇬🇧 English

🚀 **[Live Interactive Documentation (Swagger UI)](https://inventory-management-api-87vr.onrender.com/docs)**

### 🛠️ Tech Stack & Tools
* **Language:** Python 3.11+
* **Web Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM & Migrations:** SQLAlchemy 2.0 (Async) + Alembic
* **Authentication:** JWT (JSON Web Tokens) with Passlib / Bcrypt
* **Containerization:** Docker & Docker Compose
* **Deployment:** Render (Web Service + Managed PostgreSQL)

### 🏗️ Project Architecture
```text
├── app/
│   ├── api/          # Route handlers & endpoints (auth, products)
│   ├── core/         # Global settings, security (JWT) & environment variables
│   ├── db/           # Database session setup & async connection
│   ├── models/       # SQLAlchemy ORM models
│   ├── schemas/      # Pydantic schemas for data validation
│   └── main.py       # FastAPI application entry point
├── alembic/          # Database migration scripts & history
├── docker-compose.yml # Local orchestration (FastAPI + PostgreSQL)
├── Dockerfile        # Container image definition
└── requirements.txt  # Project dependencies
