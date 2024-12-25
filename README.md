# Kejarkom BRUH AuRa

Kejarkom BRUH AuRa adalah aplikasi web yang menyediakan layanan steganografi dan kriptografi untuk menyembunyikan dan mengamankan pesan. Aplikasi ini memungkinkan pengguna untuk mengenkripsi pesan, menyembunyikannya dalam gambar, dan mendekripsi pesan yang telah dienkripsi.

## Fitur

- Enkripsi dan dekripsi teks menggunakan metode kriptografi.
- Enkripsi dan dekripsi pesan dalam gambar menggunakan steganografi.
- Pengguna dapat mengunggah gambar profil dan menyimpannya.
- Antarmuka pengguna yang responsif dan mudah digunakan.
- Dukungan untuk tema gelap dan terang.

## Prerequisites

Sebelum menjalankan aplikasi ini, pastikan Anda memiliki:

- Python 3.x
- pip (package installer for Python)

## Instalasi

1. Clone repositori ini ke mesin lokal Anda:

   ```bash
   git clone https://github.com/username/repo.git
   cd repo
   ```

2. Buat dan aktifkan virtual environment (opsional tetapi disarankan):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate  # Untuk Windows
   ```

3. Install dependensi yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

   Pastikan untuk membuat file `requirements.txt` yang berisi semua dependensi yang diperlukan, seperti Flask, Pillow, dan requests.

4. Buat database SQLite:

   ```bash
   python app.py
   ```

   Ini akan membuat file `database.db` dan tabel yang diperlukan.

## Menjalankan Aplikasi

1. Jalankan server API:

   ```bash
   python api.py
   ```

2. Jalankan aplikasi utama:

   ```bash
   python app.py
   ```

3. Buka browser dan akses aplikasi di `http://127.0.0.1:5000`.

## Penggunaan

- **Enkripsi Teks**: Masukkan teks yang ingin dienkripsi dan kunci, lalu klik "Mulai Enkripsi".
- **Dekripsi Teks**: Masukkan teks terenkripsi dan kunci, lalu klik "Mulai Dekripsi".
- **Steganografi**: Unggah gambar dan masukkan pesan yang ingin disembunyikan, lalu klik "Enkripsi dengan Steganografi".
- **Dekripsi Gambar**: Unggah gambar yang berisi pesan tersembunyi dan masukkan kunci untuk mendekripsi.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request atau buka issue untuk diskusi.

## Lisensi

Proyek ini dilisensikan di bawah MIT License. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

## Kontak

Untuk pertanyaan atau informasi lebih lanjut, silakan hubungi [email@example.com](mailto:email@example.com).
