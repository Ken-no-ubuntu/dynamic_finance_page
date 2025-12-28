# 💹 Dynamic Finance Page & Engine

A full-stack financial tracking application featuring a high-performance **Rust** backend, a **PostgreSQL** database running in **Docker**, and a clean **JavaScript** frontend.

## 🏗 Project Architecture

* **Backend:** Axum (Rust) - Handles API requests and database logic.
* **Frontend:** Vanilla JS / HTML / CSS - Real-time data visualization and entry.
* **Database:** PostgreSQL (Docker) - Persistent storage for all transactions.
* **Data Tools:** Python - Reserved for future financial analysis and Bayesian modeling.

---

## 📂 Project Structure

```text
financial-engine-project/
├── backend-api/         # Rust Axum Server
│   ├── src/             # API Handlers & Database logic
│   └── migrations/      # SQL Schema definitions
├── frontend/            # Dashboard UI (HTML/JS/CSS)
├── data-tools/          # Python scripts for data analysis
├── docker-compose.yml   # Database infrastructure
└── Makefile             # Command shortcuts

```

---

## 🚀 Getting Started

### 1. Database Setup

Ensure you have Docker Desktop running. Spin up the Postgres container:

```bash
docker-compose up -d

```

### 2. Initialize the Database

Connect to the container and create the necessary tables:

```bash
docker exec -it financial_engine_db psql -U postgres -d finance

```

Inside the SQL prompt, run:

```sql
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount DOUBLE PRECISION NOT NULL,
    description TEXT NOT NULL
);

```

### 3. Start the Backend (Rust)

Navigate to the backend folder and run the server:

```bash
cd backend-api
cargo run

```

The server will start at `http://127.0.0.1:8080`.

### 4. Open the Frontend

Simply open `frontend/index.html` in your browser. You can now:

* **View** transactions (fetched via `GET /transactions`)
* **Add** new transactions (sent via `POST /transactions`)

---

## 🛠 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/health` | Check if server is alive |
| `GET` | `/transactions` | Retrieve all financial records |
| `POST` | `/transactions` | Add a new transaction (JSON body required) |

---

## 🔒 Environment Variables

Create a `.env` file in the root directory to manage your connection strings:

```env
DATABASE_URL=postgres://postgres:postgres@localhost:5432/finance

```

---

## 📝 Features

* [x] **Persistence:** Uses Docker volumes to ensure data isn't lost on restart.
* [x] **CORS Enabled:** Backend configured with `Tower-HTTP` to allow frontend communication.
* [x] **Strict Typing:** Rust `models` ensure data integrity between the DB and the UI.
