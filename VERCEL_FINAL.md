# Deploy final ke Vercel

Gunakan repository dengan file `index.py`, `requirements.txt`, dan folder `Backend` langsung di root repository.

Pengaturan Vercel:
- Framework Preset: Other
- Root Directory: `./`
- Build Command: kosong
- Output Directory: kosong
- Install Command: kosong/default

Tidak menggunakan `vercel.json` atau `pyproject.toml`.

Entry point: `index.py` yang mengekspor variabel Flask bernama `app`.
