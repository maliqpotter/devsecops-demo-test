
# TODO App (Python + FastAPI + SQLite)

A sederhana TODO app dengan FastAPI, SQLAlchemy, dan SQLite. Termasuk Dockerfile, docker-compose, dan unit test dasar (pytest). Cocok untuk belajar backend CRUD yang rapi.

## Fitur
- CRUD task: create, read (list/detail), update, delete
- Tandai complete / uncomplete
- Filter by status (completed / not completed)
- Validasi via Pydantic schemas
- SQLite (local) via SQLAlchemy
- CORS diaktifkan (opsional)
- Dockerfile + docker-compose
- Test dasar dengan pytest + httpx

## Struktur
```
todo-python/
├─ app/
│  ├─ main.py
│  ├─ database.py
│  ├─ models.py
│  ├─ schemas.py
│  └─ crud.py
├─ tests/
│  └─ test_api.py
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ .env.example
└─ README.md
```

## Cara Jalankan (tanpa Docker)
1. Buat dan aktifkan virtualenv (opsional):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan server (hot reload):
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
4. Coba API docs:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Jalankan dengan Docker
```bash
docker build -t todo-python:dev .
docker run --rm -p 8000:8000 --name todo-app todo-python:dev
# atau gunakan docker-compose:
docker compose up --build
```

## Variabel Lingkungan
Salin `.env.example` menjadi `.env` (opsional). Default sudah cukup untuk SQLite lokal.
- `DATABASE_URL` contoh: `sqlite:///./todo.db`
- `ALLOW_ORIGINS` contoh: `http://localhost:5173,http://localhost:3000` (opsional untuk front-end)

## Endpoint Utama
- `POST   /tasks`              : buat task
- `GET    /tasks`              : list task (param: `q`, `completed`)
- `GET    /tasks/{task_id}`    : detail task
- `PATCH  /tasks/{task_id}`    : update sebagian (title/description/completed)
- `DELETE /tasks/{task_id}`    : hapus task
- `POST   /tasks/{task_id}/toggle` : toggle completed

## Testing
```bash
pytest -q
```

## Lisensi
MIT
