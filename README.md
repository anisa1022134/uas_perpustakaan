# 📚 Campus Library – Sistem Basis Data Terdistribusi

Proyek ini adalah implementasi sistem basis data terdistribusi yang menggabungkan tiga jenis database berbeda:

- 🐘 **PostgreSQL**: menyimpan data peminjaman buku (relasional)
- 🍃 **MongoDB**: menyimpan ulasan dan ringkasan buku (dokumen)
- ⚡ **Redis**: menyimpan informasi ketersediaan buku (in-memory key-value)

Dikendalikan menggunakan middleware berbasis **Python**.

---

 ## 📦 Struktur Folder

# UAS Proyek Sistem Basis Data Terdistribusi

## Struktur
- `docker-compose.yml` → Orkestrasi semua container
- `ingtegrasi.py` → Python integrasi PostgreSQL + MongoDB + Redis
- `sharding_citus.sql` → Script sharding dengan Citus
- `data/seed_postgres.sql` → Isi awal data
- `doc/` → Dokumentasi (diagram, strategi, laporan)

## Cara Jalanin
1. `docker-compose up -d`
2. `psql -U postgres -d campus_library -f sharding_citus.sql`
3. `psql -U postgres -d campus_library -f data/seed_postgres.sql`
4. `python3 integrasi.py` (di container `python_client`)

# 📚 UAS - Sistem Basis Data Terdistribusi

Proyek ini merupakan implementasi **Sistem Basis Data Terdistribusi** dengan skenario `Campus Library`, yang menggabungkan teknologi:

- 🔵 PostgreSQL + Citus (Sharding & Distribusi)
- 🟢 MongoDB (Review buku)
- 🔴 Redis (Stok buku real-time)
- 🐍 Python (Integrasi data lintas sumber)

---

## 📁 Struktur Folder


