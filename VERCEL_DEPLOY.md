# Deployment Vercel — Konfigurasi Final

Gunakan Root Directory `TA_Argotelo` di dashboard Vercel.

Project ini memakai `pyproject.toml` untuk mengunci entrypoint Flask ke `index:app`. Jangan menambahkan properti `functions`, `builds`, atau `rewrites` di `vercel.json`. File `vercel.json` sengaja tidak digunakan.

Pastikan file berikut berada pada root directory yang dipilih Vercel:

- `index.py`
- `pyproject.toml`
- `requirements.txt`
- `Backend/`
- `public/`

Framework Preset: Other. Build Command dan Output Directory dikosongkan.
