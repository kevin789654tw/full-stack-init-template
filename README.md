<h1 align="center">Full Stack Boilerplate</h1>

A ready-to-use starter boilerplate for building, testing, and deploying full-stack web applications.

## Table of contents

- [Introduction](#introduction)
  - [Key Features](#key-features)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)

## Introduction

This repository is a ready-to-use starter boilerplate designed to accelerate full-stack web application development. It combines a modern frontend, a robust backend API, and a containerized environment to streamline setup, development, and deployment.

With its clear structure and preconfigured environment management, this boilerplate is ideal for prototyping, team projects, or production-ready applications.

### Key Features

This project provides a solid foundation for building, testing, and deploying full-stack applications. The core features include:

- **🚢 Containerized Architecture:** Uses Docker Compose to orchestrate interconnected services like PostgreSQL, backend API, and frontend, ensuring consistent environments.

- **🎨 Modern Frontend:** Integrates React, Vite, Tailwind CSS, and TypeScript for a fast, styled, and maintainable user interface.

- **🛠️ Backend API:** Built with FastAPI, supporting efficient data handling and RESTful endpoints.

- **🗂️ Organized Structure:** Facilitates scalable development with clear separation of frontend and backend components.

- **⚙️ Environment Management:** Provides templates and configurations for seamless environment setup across development and production.

### Built With

- **Frontend:** ⚛️ React, ⚡ Vite, 🎨 Tailwind CSS, 📝 TypeScript
- **Backend:** 🚀 FastAPI, 🐍 Python
- **Database:** 🗄️ PostgreSQL
- **Containerization:** 🐳 Docker, 🔗 Docker Compose
- **Environment Management:** 🌱 `.env` templates, ⚙️ preconfigured configurations

<br/>

## Getting started

### Installation

Build fullstack-boilerplate from the source and install dependencies:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kevin789654tw/fullstack-boilerplate.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd fullstack-boilerplate
   ```

3. **Set up environment variables:**
   ⚠️ (replace placeholders with your own secrets, do not commit sensitive data) ⚠️

   ```bash
   cp .env.example .env
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env.development
   cp frontend/.env.example frontend/.env.production  # comment out localhost and uncomment your backend URL
   ```

### Usage

Run the project with:

1. **Using [Docker Compose](https://docs.docker.com/compose/):**

   ```bash
   docker compose up --build
   ```

<br/>

---

### 🚀 More details will be coming soon 🚀
