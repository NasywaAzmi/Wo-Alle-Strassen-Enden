Algoritma: Menggunakan algoritma jumpsearch

Fungsionalitas: Fungsionalitas utama program Jump Search untuk mengurangi pengecekan data seperti linear search dimana jump search
menggunakan metode lompat secara teratur untuk menemukan data yang dicari.

Elemen: Program jumpsearch menggunakan elemen len, min

Cara kerja:

  1.  program akan menerima inputan berupa data yang ingin dicari dan array yang berisi data yang terurut.
  
  2.  Program akan menghitung ukuran blok dengan menggunakan rumus √n, dimana n itu adalah ukuran array.
  
  3.  Program akan mengambil blok data pertama sebagai acuan pencarian.
  
  4.  Program memeriksa data yang ada pada akhir blok untuk menentukan apakah data yang dicari berada di dalam blok atau tidak.
  
  5.  Program melompat ke blok berikutnya dengan menggunakan teknik jump.
  
  6.  Program melakukan langkah 4 dan 5 secara berulang-ulang pada blok yang dipilih hingga data yang dicari ditemukan atau tidak ditemukan.
  
  7.  Jika data yang dicari telah ditemukan, program mengembalikan indeks dari data tersebut. Jika data tidak ditemukan, program memberikan pesan error.
