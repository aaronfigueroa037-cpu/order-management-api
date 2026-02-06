# Order Management API

A RESTful backend API built with FastAPI that demonstrates secure user authentication, 
role-based authorization, and database-backed user management.


This project is designed as a portfolio-grade backend system showcasing real-world 
API patterns such as JWT authentication, protected routes, and admin-only access.

---

## ▶ How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/order-management-api.git
cd order-management-api

## 🔐 Security & Production Readiness Notes

This project is designed for local development and learning purposes.

For a production deployment, the following improvements would be applied:

- Environment variables (`.env`) for secrets (JWT secret key, database URL)
- Token expiration and refresh token strategy
- HTTPS enforcement
- Rate limiting on authentication endpoints
- Centralized logging and monitoring
- Database migrations (Alembic)
- Pagination for large result sets
- Role-based access expansion (admin/editor/user)


## 🔐 Authentication Flow (JWT)

This API uses **JWT (JSON Web Tokens)** for secure authentication and authorization.

The authentication process follows these steps:

### 1️⃣ Register a New User

Create a user account using the registration endpoint.

**Endpoint**

**Request Body**
```json
{
  "name": "Test User",
  "email": "testuser@example.com",
  "password": "securepassword"
}

---

```md
### 2️⃣ Login and Receive Access Token

Authenticate using your email and password to receive a JWT access token.

**Endpoint**

**Form Data**

**Response**
```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}

---

```md
### 3️⃣ Access Protected Routes

Use the access token in the `Authorization` header:

Without this token, protected endpoints will return:

```json
{
  "detail": "Not authenticated"
}

---

```md
### 4️⃣ Get Current Authenticated User

Retrieve the currently logged-in user.

**Endpoint**

**Authorization Required**

**Response**
```json
{
  "id": 1,
  "name": "Test User",
  "email": "testuser@example.com",
  "is_admin": false
}

---

md
### 5️⃣ Admin-Only Access

Some endpoints are restricted to admin users only.

**Example**

Only users with `is_admin = true` can access this endpoint.

If a non-admin user attempts access, the API returns:

```json
{
  "detail": "Admin access required"
}

## 🎯 Project Goals

This project was built to demonstrate real-world backend concepts commonly required 
for internships and junior backend roles, including:

- Secure authentication using JWT
- Role-based access control (admin vs user)
- Clean API structure using FastAPI routers
- Database-backed persistence with SQLAlchemy

---

## Features

- **FastAPI** routing + Swagger UI (`/docs`)
- **SQLAlchemy** ORM models
- **SQLite** database for local development
- **Password hashing (bcrypt)**
- **JWT authentication**
- **Protected routes (Bearer token required)**
- **Admin-only routes** (authorization enforced via FastAPI dependencies)
- Proper HTTP codes:
  - **401 Unauthorized** → not logged in / invalid token  
  - **403 Forbidden** → logged in but not allowed (not admin)

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- passlib (bcrypt)
- python-jose (JWT)
- Uvicorn
- SQLite

---

## Project Structure

```text
order-management-api/
├─ app/
│  ├─ main.py              # FastAPI app entrypoint
│  ├─ database.py          # DB engine + SessionLocal
│  ├─ models.py            # SQLAlchemy models
│  ├─ schemas.py           # Pydantic schemas
│  ├─ auth.py              # hashing + JWT + auth dependencies
│  └─ routes/
│     ├─ users.py          # user routes (some protected/admin-only)
│     └─ ...               # other routes (if added)
├─ requirements.txt
└─ README.md
