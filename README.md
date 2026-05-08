# TODO App (DevSecOps Demo)

A sederhana TODO app dengan FastAPI, SQLAlchemy, dan SQLite. Proyek ini dikonfigurasi untuk demonstrasi **DevSecOps Pipeline** yang komprehensif.

## Struktur Proyek
- `app/`: Source code FastAPI (Models, CRUD, Schemas)
- `.github/workflows/`:
  - `ci.yml`: Scan keamanan otomatis pada setiap Pull Request.
  - `cd.yml`: Build, Image Scan (Trivy), dan DAST (ZAP) pada push ke branch `main`.

---

## Pengujian Lokal (DevSecOps di Local)

Sebelum melakukan `push`, sangat disarankan untuk menjalankan pengujian berikut di mesin lokal:

### 1. Persiapan Environment
```bash
# Buat virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependensi aplikasi & tool pengujian
pip install -r requirements.txt
pip install ruff bandit pip-audit pytest pytest-cov
```

### 2. Jalankan Pemindaian Keamanan & Kualitas Kode
Jalankan perintah berikut secara berurutan:

*   **Linting (Ruff)**: Memastikan standar penulisan kode.
    ```bash
    ruff check .
    ```
*   **SAST (Bandit)**: Mencari celah keamanan pada kode source.
    ```bash
    bandit -r app
    ```
*   **SCA (pip-audit)**: Memeriksa kerentanan pada library pihak ketiga.
    ```bash
    pip-audit -r requirements.txt
    ```
*   **Unit Testing (pytest)**: Menjalankan test fungsional dan cakupan kode.
    ```bash
    PYTHONPATH=. pytest --cov=app
    ```

### 3. Pengujian Container (Docker)
Jika Anda memiliki Docker terinstal, Anda bisa menguji image secara lokal:
```bash
# Build image
docker build -t todo-app:local .

# Jalankan container
docker run -d -p 8000:8000 --name todo-test todo-app:local

# (Opsional) Scan image menggunakan Trivy (jika terinstal)
trivy image todo-app:local
```

---

## Fitur DevSecOps Terpasang
1.  **Non-root User**: Container berjalan sebagai user terbatas (keamanan runtime).
2.  **Security Headers**: Dilengkapi dengan CSP, HSTS, X-Frame-Options, dll.
3.  **Strict Pipeline**: Pipeline akan gagal jika ditemukan isu keamanan baru (proteksi otomatis).
4.  **SBOM**: Menghasilkan daftar komponen (Software Bill of Materials) di setiap build.

## Lisensi
MIT
