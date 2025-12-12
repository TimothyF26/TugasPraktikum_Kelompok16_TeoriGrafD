# Knight's Tour Solver (Python)

Program Python ini dibuat untuk menyelesaikan permasalahan Knight's Tour pada papan catur berukuran 8x8 menggunakan algoritma Backtracking yang dioptimasi dengan heuristik (Warnsdorff-like ordering). Program juga menyediakan visualisasi grafis dari perjalanan kuda menggunakan matplotlib.

---

## Deskripsi Singkat

Knight's Tour adalah permasalahan klasik dalam teori graf dan algoritma, di mana sebuah bidak kuda harus mengunjungi setiap kotak papan catur tepat satu kali. Terdapat dua jenis tour:

1. Open Tour  
   Kuda mengunjungi semua kotak tanpa harus kembali ke posisi awal.

2. Closed Tour  
   Kuda mengunjungi semua kotak dan langkah terakhir dapat kembali menyerang posisi awal, membentuk siklus.

Program ini menerima input dari pengguna, menjalankan pencarian solusi menggunakan backtracking dengan prioritas langkah berdasarkan derajat (jumlah langkah valid berikutnya), dan menghasilkan dua jenis output: representasi matriks langkah dan visualisasi grafis.

---

## Input Program

Saat program dijalankan, pengguna diminta memasukkan tiga data secara berurutan:

1. Jenis Tour  
   - Ketik `open` untuk Open Tour  
   - Ketik `closed` untuk Closed Tour

2. Posisi Baris Awal (Row / X)  
   Masukkan angka dari 0 sampai 7.

3. Posisi Kolom Awal (Column / Y)  
   Masukkan angka dari 0 sampai 7.

Catatan:  
Koordinat (0, 0) merepresentasikan pojok kiri atas papan catur.

---

## Output Program

Jika solusi ditemukan, program menghasilkan dua jenis output:

### 1. Representasi Matriks (Terminal)

Program mencetak papan catur 8x8 dalam bentuk matriks berisi angka 0 hingga 63.

- Angka 0 adalah posisi awal.
- Langkah-langkah berikutnya ditandai dengan angka 1, 2, 3, dan seterusnya.

Contoh:
```
 0 59 38 33 30 17  8 63
37 34 31 60  9 62 29 16
58  1 36 39 32 27 18  7
35 48 41 26 61 10 15 28
42 57  2 49 40 23  6 19
47 50 45 54 25 20 11 14
56 43 52  3 22 13 24  5
51 46 55 44 53  4 21 12
```

### 2. Visualisasi Grafis (Matplotlib Window)

Program menampilkan jendela grafik yang berisi:

- Garis yang menghubungkan seluruh langkah kuda.
- Titik awal perjalanan ditandai dengan marker berbentuk bintang berwarna merah.
- Papan ditampilkan tanpa grid catur (agar fokus pada jalur gerakan).

---

## Metode dan Algoritma

Program menggunakan pendekatan berikut:

1. Backtracking  
   Menelusuri seluruh kemungkinan langkah secara rekursif.

2. Validasi Gerakan  
   Fungsi `is_valid_move()` memastikan kuda hanya melangkah ke kotak dalam papan dan belum pernah dikunjungi.

3. Heuristik Degree Ordering  
   Fungsi `get_degree()` menghitung jumlah langkah valid dari langkah kandidat.  
   Kandidat dengan degree terkecil dicoba lebih dahulu (heuristik ala Warnsdorff).

4. Closed Tour Checking  
   Untuk closed tour, langkah terakhir harus dapat kembali menyerang posisi awal.

5. Visualisasi  
   Menggunakan matplotlib untuk menggambar jalur berdasarkan urutan langkah dalam matriks.

---

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Pastikan matplotlib sudah tersedia. Jika belum, install dengan:
   ```bash
   pip install matplotlib
   ```
3. Jalankan program melalui terminal:
   ```bash
   python nama_file.py
   ```
4. Masukkan input sesuai instruksi di terminal.

---

## Dependensi

Program ini menggunakan:

- `sys`
- `matplotlib`

Tidak ada library eksternal lain seperti pygame yang digunakan.

---

## Catatan

- Pada beberapa posisi awal dan jenis tour, solusi mungkin tidak ditemukan (terutama closed tour).
- Rekursi menggunakan peningkatan batas melalui `sys.setrecursionlimit()` karena kedalaman pencarian yang besar.

---

## Lisensi

Proyek ini dibuat untuk kebutuhan pembelajaran dan eksplorasi algoritma klasik. Bebas digunakan dan dimodifikasi.


# Largest Monotonically Increasing Subsequence (LMIS)

Program Python ini dibuat untuk menemukan sub-urutan naik terpanjang (Largest Monotonically Increasing Subsequence / LMIS) dari sekumpulan angka acak. Solusi diimplementasikan menggunakan struktur data Tree dan algoritma rekursif (DFS) untuk mengeksplorasi semua kemungkinan jalur urutan naik.

---

## Input Program

Input tidak diambil dari pengguna, melainkan didefinisikan langsung di dalam kode.

Default Sequence:
```python
[4, 1, 13, 7, 0, 2, 8, 11, 3]
```

Modifikasi Input:
Anda dapat mengubah isi list `input_sequence` pada file tugas_LMIS.py untuk menguji urutan angka lainnya.

---

## Output Program

Saat dijalankan, program akan menampilkan:

1. Urutan Angka Input  
   Menampilkan kembali urutan angka awal yang diproses.

2. Panjang LIS  
   Menampilkan jumlah elemen dari sub-urutan naik terpanjang yang ditemukan.

3. Salah Satu LIS  
   Contoh hasil urutan naik terpanjang, misalnya:
   ```
   [4, 7, 8, 11]
   ```

4. Penjelasan Metode  
   Deskripsi singkat mengenai cara kerja Tree dan DFS untuk menemukan LMIS.

---

## Metode yang Digunakan

Program membangun sebuah struktur Tree yang berisi seluruh kemungkinan jalur sub-urutan naik. Prinsip kerjanya:

- Setiap angka dapat menjadi node awal atau bagian dari jalur.
- Cabang baru hanya dibuat jika angka berikutnya lebih besar dari angka saat ini.
- DFS digunakan untuk menelusuri semua jalur.
- Jalur terpanjang dipilih sebagai hasil Largest Monotonically Increasing Subsequence.

Pendekatan ini memberikan gambaran struktural dari proses pencarian LIS.

---

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Buka terminal atau command prompt.
3. Jalankan:
   ```bash
   python tugas_LMIS.py
   ```
4. Hasil akan muncul di console.

---

## Catatan

Anda bebas memodifikasi input sequence dan mengeksplorasi pengembangan algoritma Tree untuk analisis lebih lanjut.