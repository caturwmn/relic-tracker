## Tugas 3

1. Form POST berfungsi untuk menambahkan suatu data ke dalam page dimana data dari form tersebut akan disimpan ke server dan tidak bisa dibaca oleh user kecuali data tersebut ditampilkan di page secara langsung
   sedangkan Form GET akan menghasilkan data yang disimpan dalam bentuk berupa url dari page yang disisipkan permintaan pengguna sehingga bisa mudah di akses jika di bookmark, namun kurang aman karena bisa       
   dilihat secara langsung melalui url-nya

2. Perbedaannya antara lain
  - Dalam penyimpanan data, JSON baik untuk menyimpan data terkait objek dan lebih mudah dibaca karena tidak perlu menggunakan end tag, JSON juga bisa menggunakan array dan memiliki performa lebih baik untuk penggunaan AJAX
  - Jika dibandingkan dengan JSON, XML lebih baik untuk menyimpan suatu kumpulan data yang terstruktur. XML juga lebih aman, bisa memiliki namespace agar tidak terjadi konflik pada data, bisa dimasukkan dengan comment untuk penjelasan kode jika diperlukan, serta bisa memakai Encoding selain UTF-8
  - HTML Sendiri lebih berguna untuk menjadi format dasar penampilan suatu page karena bisa menampilkan data secara terstruktur dan fungsi utamanya memang untuk ditampilkan pada web (bisa memiliki header dll).

3. JSON Sering digunakan untuk transfer data karena jika dibandingkan dengan XML, JSON lebih ringan terutama jika suatu web memanfaatkan AJAX yang memungkinkan web asinkronus. JSON sendiri berasal dari bahasa JavaScript sehingga proses konversi JSON ke JavaScript cepat.

4. Langkah-Langkah Implementasi:
- Pertama, membuat sebuah base template dan meroute template tersebut melalui settings.py dan mengatur template lainnya untuk mengikuti (atau mengextend) base template tersebut
- Lalu, membuat file forms.py yang berisi class form dan class metadata yang berisi informasi tentang jenis item yang akan dibuat beserta atribut-atribut yang perlu diisi secara manual
- Terus membuat fungsi baru untuk membuat item baru dengan menggunakan forms.py dan model form yang digunakan di views.py dan menghubungkannya ke sebuah template baru yang berisi format penampilan form beserta tombol pembuatan item yang diinginkan.
- Lalu sesuaikan main.html agar bisa menampilkan data dari item yang dimiliki
- Lalu membuat 4 fungsi baru dengan memanfaatkan HTTPResponse dan Serializers untuk mengubah data yang diinginkan menjadi data XML, data JSON, serta kedua fungsi tersebut yang menerima id dari data dan melakukan routing pada urls.py agar dapat mengakses tiap halaman yang digunakan oleh fungsi-fungsi tersebut(termasuk create item jika belum

5. Screenshot:
-main
![](misc/main.png)

- xml
![](misc/xml.png)

- xml with id
![](misc/xmlid.png)

- json
![](misc/json.png)

- json with id
![](misc/jsonid.png)

------------------------------

## Tugas 2

# relic-tracker
[Relic Tracker Link](https://relic-tracker.adaptable.app/main/)
---

Langkah-langkah Implementasi:
1. Membuat proyek django baru :
- Dilakukan dengan membuat direktori dengan nama yang diinginkan
- Menyusun daftar aplikasi yang diperlukan (termasuk django)
- Menginstallnya menggunakan pip install di virtual environment
- Menginisiasi proyek dengan django-admin startproject (namaproyek) .
- Lalu mensetting allowed hostu

2. Membuat aplikasi baru bernama main
- Pergi ke cli dan ketik (di venv) python manage.py startapp main

3. Melakukan routing pada proyek agar menjalankan apliikasi main :
- Pergi ke settings.py proyek dan masukkan main ke dalam list INSTALLED_APPS

4. Membuat model pada aplikasi main dengan nama Item:
Mengubah isi models.py pada main dan memasukkan:
- From django.db import models jika belum ada
- Lalu inisiasi class Item dengan Class Item(models.Model) :
- Lalu tambahkan atribute didalamnya dengan nama_atribute = ditambah: 
  models.CharField untuk charfield
  models.DateField untuk Datefield
  dan seterusnya
- Terakhir, melakukan migration 

5. Membuat fungsi pada views.py:
- Jika belum membuat main.html yang berisi data nama, kelas, dan app pada direktori templates di main, maka di buat dulu
- Setelah itu buka views.py pada main dan isi dengan:
  from django.shortcuts import render jika belum ada
  Lalu, tambahkan fungsi show_main yang berisi context dengan parameter request
  Context berisi data yang akan menggantikan field data pada template
  Fungsi mereturn render(request, 'nama_template', context)
  Jika belum, ubahlah data pada templates dengan data field ({{ data }}) yang sesuai

6. Routing urls.py:
- Buat file urls.py pada file app (main) dan import path dari django.urls, dan fungsi
- show_main (atau fungsi render lain) dari main.views atau .views
- masukan app_name = 'main'
- dan masukan urlpatterns = \[path('', show_main, name='show_main')]
- pindah ke urls.py di file proyek yang mengatur interaksi aplikasi dengan web
- tambahkan include disamping import path yang sudah ada
- lalu masukan path('main/', include('main.urls')) pada urlpatterns

7. Deploy app adaptable:
- buat aplikasi baru di adaptable dengan menggunakan repositori proyek
- gunakan template python, dan hosting PostgreSQL
- sesuaikan versi python dan tambahkan start command
  python manage.py migrate && gunicorn (nama proyek).wsgi
- centangkan HTTP listener dan tunggu

8. Buat README.md:
- tinggal add file README.md di direktori dan add commit push

Bagan MVT Django:
![](misc/chart.png)


Virtual Environtment:
- Virtual environtment kita gunakan dalam pembuatan proyek django agar project 
kita bisa berjalan dengan menggunakan file-file yang memiliki versi python atau django yang berbeda-beda
- Selama kita tidak menggunakan file yang menggunakan versi python atau django yang berbeda-beda, seharusnya
kita tetap bisa membuat aplikasi web, namun jika kita menggunakan file dengan versi django yang berbeda, akan
terjadi banyak error

MVC(Model View Controller)
- MVC adalah pola desain software dimana digunakannya komponen berupa controller yang mengendalikan hubungan antara model dan view serta sekaligus menjadi pusat aplikasi yang menerima permintaan dari user melalui view dan mengubah model berdasarkan permintaan. Model menyimpan data dan view menampilkan UI untuk pengguna. Tiap bagian pada MVC terikat erat sehingga susah di modifikasi. Baik untuk proyek skala kecil

MVT(Model View Template)
- MVT adalah pola desain web dimana digunakannya views untuk menerima dan membalikan request dari pengguna melalui template yang menjadi bagian yang menampilkan data dalam bentuk kode html. Karena bagian-bagiannya tidak terikat erat, modifikasi mudah. Bagian yang dilakukan oleh controller pada MVC di tangani oleh framework pada MTV. Model juga tetap bekerja sebagai penyimpanan data atau database. Baik untuk proyek kecil dan besar.

MVVM(Model View ViewModel)
- MVVM adalah pola desain software dimana digunakannya ViewModel yang berfungsi sebagai hubungan dari view dan model dimana bagian view hanya bekerja untuk menerima input pengguna dan membalikan data yang sesuai dari viewmodel. Viewmodel sendiri menerima input dari view dan menyampaikannya ke model dan mengirim balasan dari model ke view. Model tetap bekerja sebagai database. mudah di modifikasi namun bisa susah untuk dilakukan 'debugging'. Baik untuk proyekk skala besar
