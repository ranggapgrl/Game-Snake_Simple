# 🐍 Python Snake Game Sederhana

Sebuah game Snake klasik yang dibangun sepenuhnya menggunakan bahasa pemrograman Python dan library bawaan `turtle`. Proyek ini sangat cocok dimainkan untuk nostalgia atau dijadikan referensi dalam mempelajari logika dasar pengembangan game 2D.

## ✨ Fitur

* **Gameplay Klasik:** Mekanik permainan yang familier, makan *food* untuk bertambah panjang.
* **Sistem Skor Dinamis:** Dilengkapi dengan pelacak *Score* saat ini dan pencatat *High Score* tertinggi.
* **Tingkat Kesulitan Progresif:** Kecepatan ular (delay) akan otomatis bertambah sedikit demi sedikit setiap kali memakan *food*, memberikan tantangan lebih seiring berjalannya waktu.
* **Deteksi Tabrakan Presisi:** Game akan otomatis ter-reset jika kepala ular menabrak batas dinding layar atau menabrak ekornya sendiri.
* **UI Bersih:** Tampilan antarmuka yang simpel tanpa tumpang tindih teks.

## 🛠️ Teknologi yang Digunakan

* **Bahasa:** Python 3.x
* **Library:** `turtle` (Grafis dasar), `time` (Pengatur waktu/delay), `random` (Pengacak posisi makanan)

## 🎮 Cara Menjalankan Game

Karena game ini menggunakan library bawaan standar, kamu tidak perlu menginstal *dependency* eksternal tambahan.

1.  Pastikan kamu sudah menginstal **Python** di komputermu.
2.  *Clone* repositori ini atau *download* file `.py`-nya:
    ```bash
    git clone [https://github.com/username-kamu/nama-repo.git](https://github.com/username-kamu/nama-repo.git)
    ```
3.  Buka terminal/Command Prompt dan arahkan ke direktori tempat file disimpan.
4.  Jalankan perintah berikut:
    ```bash
    python snake_game.py
    ```

*(Catatan: Sesuaikan nama file `snake_game.py` dengan nama file utamamu jika berbeda).*

## ⌨️ Kontrol Permainan

Pastikan jendela *keyboard* aktif dalam bahasa Inggris (bukan Capslock aktif) saat bermain.

* `W` - Bergerak ke Atas
* `S` - Bergerak ke Bawah
* `A` - Bergerak ke Kiri
* `D` - Bergerak ke Kanan

## 👨‍💻 Author

Dikembangkan oleh pgrl

Jangan ragu untuk melakukan *fork*, memberikan *star*, atau memodifikasi kode ini untuk bereksperimen dengan fitur-fitur baru!
