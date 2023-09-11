# relic-tracker
[Relic Tracker Link](https://relic-tracker.adaptable.app/)
---

Langkah-langkah Implementasi:
1. Membuat proyek django baru :
- Dilakukan dengan membuat direktori dengan nama yang diinginkan
- Menyusun daftar aplikasi yang diperlukan (termasuk django)
- Menginstallnya menggunakan pip install di virtual environment
- Menginisiasi proyek dengan django-admin startproject (namaproyek) .
- Lalu mensetting allowed hostu

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

7.Deploy app adaptable:
- buat aplikasi baru di adaptable dengan menggunakan repositori proyek
- gunakan template python, dan hosting PostgreSQL
- sesuaikan versi python dan tambahkan start command
  python manage.py migrate && gunicorn (nama proyek).wsgi
- centangkan HTTP listener dan tunggu

8. Buat README.md:
- tinggal add file README.md di direktori dan add commit push
