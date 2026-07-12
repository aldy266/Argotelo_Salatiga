# Tindakan Keamanan Sebelum Deploy

Repository GitHub lama bersifat publik dan riwayat Git pada arsip awal pernah memuat `Backend/.env` serta key yang ditulis langsung di source code. Menghapus file pada commit terbaru tidak menghapus data dari commit lama.

## Wajib dilakukan

1. Rotasi password/user TiDB yang digunakan aplikasi.
2. Rotasi Cloudinary API Secret.
3. Rotasi Resend API Key.
4. Rotasi Midtrans Server Key dan Client Key.
5. Buat `SECRET_KEY` Flask baru.
6. Masukkan semua nilai baru hanya melalui Vercel Environment Variables.

## Cara paling aman dan mudah

Buat repository GitHub **baru** dari folder bersih ini, lalu hubungkan repository baru tersebut ke Vercel. Folder ini tidak membawa `.git` dan tidak membawa `.env`, sehingga riwayat lama tidak ikut terunggah.

```powershell
cd TA_Argotelo
git init
git add .
git commit -m "Initial clean Vercel deployment"
git branch -M main
git remote add origin https://github.com/USERNAME/NAMA-REPO-BARU.git
git push -u origin main
```

Set repository menjadi private jika source code tidak ditujukan untuk publik.
