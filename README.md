Knight's Tour

Program Python ini dibuat untuk menyelesaikan permasalahan The Knight's Tour pada papan catur dimensi 8×8 menggunakan algoritma Backtracking yang dioptimasi dengan heuristik. Program juga menyertakan visualisasi grafis jalur perjalanan kuda.


Input Program

Pengguna akan diminta memasukkan tiga data berikut secara berurutan:

    Jenis Tour (Type):

        Ketik open: Kuda mengunjungi semua kotak tepat satu kali (titik akhir bebas).

        Ketik closed: Kuda mengunjungi semua kotak dan titik akhir dapat kembali menyerang titik awal (membentuk siklus/loop).

    Posisi Baris Awal (Row / X):

        Masukkan angka 0 sampai 7.

    Posisi Kolom Awal (Column / Y):

        Masukkan angka 0 sampai 7.

    Catatan: Koordinat (0, 0) merepresentasikan pojok kiri atas papan catur.

Output Program

Jika solusi ditemukan, program akan memberikan dua jenis luaran:

    Representasi Matriks (Terminal): Menampilkan papan catur 8×8 berisi angka 0 sampai 63. Angka 0 adalah posisi awal, diikuti langkah ke-1, ke-2, dst.

    Visualisasi Grafis (Pop-up Window): Akan muncul jendela baru yang menampilkan grafik perjalanan kuda:

        Garis Biru: Jalur pergerakan kuda.

        Bintang Merah: Titik awal keberangkatan.


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