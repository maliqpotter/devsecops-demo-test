# TODO App (DevSecOps Demo)

A sederhana TODO app dengan FastAPI, SQLAlchemy, dan SQLite. Proyek ini dikonfigurasi untuk demonstrasi **DevSecOps Pipeline** dengan skenario *Fail-Fast*.

## Struktur Proyek
- `app/`: Source code FastAPI
- `.github/workflows/`:
  - `ci.yml`: Scan keamanan pada setiap Pull Request.
  - `cd.yml`: Build, Scan Image, dan DAST (ZAP) pada push ke `main`.

---

## Skenario Demo: Fail vs Success

### 1. Tahap ERROR (Skenario Gagal)
Secara default, kode saat ini mengandung beberapa celah yang akan membuat pipeline **Gagal (Merah)**:

| Alat Scan | Penyebab Gagal | Lokasi |
| :--- | :--- | :--- |
| **Ruff** | Unused import `json` | `app/main.py` |
| **Bandit** | Vulnerability `subprocess` dengan `shell=True` | `app/main.py` |
| **Gitleaks** | Hardcoded AWS Secret Key | `app/main.py` |
| **pip-audit** | Versi `requests==2.20.0` yang rentan | `requirements.txt` |
| **Checkov** | Menjalankan container sebagai `root` | `Dockerfile` |

### 2. Tahap SUCCESS (Cara Memperbaiki)
Untuk membuat pipeline menjadi **Hijau (Berhasil)**, lakukan perubahan berikut:

1.  **Fix Lint & Secrets**:
    - Hapus `import json` di `app/main.py`.
    - Hapus baris `SECRET_KEY = "AKIA..."` di `app/main.py`.
2.  **Fix SAST**:
    - Hapus endpoint `/debug/ping` atau ganti logika `subprocess` agar lebih aman.
3.  **Fix SCA**:
    - Hapus `requests==2.20.0` dari `requirements.txt` (atau update ke versi terbaru).
4.  **Fix IaC**:
    - Di `Dockerfile`, hapus baris `USER root` agar kembali menggunakan `USER appuser`.

---

## Cara Menjalankan Lokal
1. Install deps: `pip install -r requirements.txt`
2. Run app: `uvicorn app.main:app --reload`
3. Test: `pytest`

## Pipeline DevSecOps
- **CI**: Mendeteksi masalah keamanan sebelum kode masuk ke branch utama.
- **CD**: Memastikan artifact (Docker image) aman dan melakukan scan dinamis (DAST) pada aplikasi yang sedang berjalan secara lokal di runner.
