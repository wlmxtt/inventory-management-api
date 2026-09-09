# Inventory Management API 📦

An asynchronous RESTful API for inventory management and stock control, built with **FastAPI**, **SQLAlchemy (Async)**, **Alembic**, and **PostgreSQL**. The project is containerized using **Docker** and deployed to the cloud via **Render**.

🌐 **Languages:** [English](#-english) | [Español](#-español)
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
```

### 🔑 Key Features
* **Secure Authentication:** User registration and login flow protected by OAuth2 / JWT access tokens.
* **Product CRUD:** Complete resource management with strict data validation powered by Pydantic.
* **Asynchronous I/O:** Non-blocking database queries leveraging `asyncpg` and SQLAlchemy's `ext.asyncio`.
* **Automated Migrations:** Database schema migrations executed on container startup via Alembic.

### ⚙️ Local Setup with Docker
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/wlmxtt/inventory-management-api.git](https://github.com/wlmxtt/inventory-management-api.git)
   cd inventory-management-api

2. **Run the application stack:**
   ```bash
   docker compose up --build -d

3. **Access local endpoints:**
   * **Swagger UI:** [`http://localhost:8000/docs`](http://localhost:8000/docs)
   * **ReDoc:** [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

 ### 🌐 Cloud Deployment
* **Base URL:** [`https://inventory-management-api-87vr.onrender.com`](https://inventory-management-api-87vr.onrender.com)
* **Swagger Docs:** [`https://inventory-management-api-87vr.onrender.com/docs`](https://inventory-management-api-87vr.onrender.com/docs)    
---

<a id="espanol"></a>
## 🇪🇸 Español

🚀 **[Ver Documentación Interactiva (Swagger UI)](https://inventory-management-api-87vr.onrender.com/docs)**

### 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.11+
* **Framework Web:** FastAPI
* **Base de Datos:** PostgreSQL
* **ORM y Migraciones:** SQLAlchemy 2.0 (Async) + Alembic
* **Autenticación:** JWT (OAuth2) con Passlib / Bcrypt
* **Containerización:** Docker & Docker Compose
* **Despliegue:** Render (Web Service + PostgreSQL gestionado)

### 🏗️ Arquitectura del Proyecto
```text
├── app/
│   ├── api/          # Controladores de rutas y endpoints (auth, productos)
│   ├── core/         # Configuración global, seguridad (JWT) y variables de entorno
│   ├── db/           # Configuración de sesión y conexión asíncrona
│   ├── models/       # Modelos del ORM SQLAlchemy
│   ├── schemas/      # Esquemas de Pydantic para validación de datos
│   └── main.py       # Punto de entrada de la aplicación FastAPI
├── alembic/          # Historial y scripts de migraciones de la base de datos
├── docker-compose.yml # Orquestación local (FastAPI + PostgreSQL)
├── Dockerfile        # Definición de la imagen del contenedor
└── requirements.txt  # Dependencias del proyecto
```


### 🔑 Características Principales
* **Autenticación Segura:** Flujo de registro e inicio de sesión protegido con tokens de acceso OAuth2 / JWT.
* **CRUD de Productos:** Gestión completa de recursos con validación estricta de datos mediante Pydantic.
* **I/O Asíncrono:** Consultas no bloqueantes a la base de datos utilizando `asyncpg` y `ext.asyncio` de SQLAlchemy.
* **Migraciones Automáticas:** Ejecución de migraciones en la base de datos durante el arranque del contenedor mediante Alembic.

### ⚙️ Instalación Local con Docker
1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/wlmxtt/inventory-management-api.git](https://github.com/wlmxtt/inventory-management-api.git)
   cd inventory-management-api

2. **Levantar el entorno con Docker Compose:**
   ```bash
   docker compose up --build -d

3. **Acceder a los endpoints locales:**
   * **Swagger UI:** [`http://localhost:8000/docs`](http://localhost:8000/docs)
   * **ReDoc:** [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

### 🌐 Despliegue en la Nube
* **URL Base:** [`https://inventory-management-api-87vr.onrender.com`](https://inventory-management-api-87vr.onrender.com)
* **Swagger Docs:** [`https://inventory-management-api-87vr.onrender.com/docs`](https://inventory-management-api-87vr.onrender.com/docs)
