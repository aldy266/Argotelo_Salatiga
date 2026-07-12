# Deployment final Vercel

Entrypoint Flask berada di `api/index.py` dan seluruh route diarahkan ke fungsi tersebut melalui `vercel.json`.

Pengaturan Vercel:
- Root Directory: folder yang langsung berisi `api`, `Backend`, `public`, `requirements.txt`, dan `vercel.json`.
- Framework Preset: Other.
- Build Command: kosong.
- Output Directory: kosong.
- Install Command: default.
