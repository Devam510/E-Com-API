# E-Commerce Backend API

A complete e-commerce backend built with FastAPI, PostgreSQL, and JWT authentication.

## Features

- User authentication (JWT)
- Product management (Admin only)
- Order processing
- Inventory management
- Auto-generated API documentation

## Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT
- **Deployment**: Docker, Render/Railway ready

## Quick Start

1. Clone the repository
2. Copy `.env.example` to `.env` and update variables
3. Run with Docker:
   ```bash
   docker-compose up --build