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
