"""
 Mohammad Arfan Nur Rahman
 mohammadarfan1234@gmail.com
 NRP 5009221073
"""

# NOTE:
# library yang dibutuhkan : numpy, matplotlib, requests

# import library numpy
import numpy as np

# import library matplotlib
import matplotlib.pyplot as plt

# import library requests untuk scrapping data dari internet
import requests

# import json untuk mengconvert json ke array atau dictionary
import json

# mengambil data dari https://data.covid19.go.id/public/api/update.json
req = requests.get('https://data.covid19.go.id/public/api/update.json').content

# menampilkan data
plt.title('Data COVID-19 Harian')

# menyiapkan list kosong yang nantinya untuk menampung data hari ke berapa,
# jumlah kasus positif jumlah orang meninggoy, jumlah orang yang sembuh,
#  jumlah orang yang dirawat
date = []
jum_positif = []
jum_meninggoy = []
jum_sembuh = []
jum_dirawat = []

# parsing data dari json menjadi array / dictionary
json = json.loads(req)

# membuat looping untuk membaca data update harian yang ada di dalam variable json
for x in range(0, len(json['update']['harian'])):
    # membuat variable untuk menyingkat key yang dipanggil
    data = json['update']['harian'][x]
    # menambahkan data hari ke berapa ke variable date
    # NOTE:  diberi + 1 karena pada looping data dimulai dari 0, sedangkan
    #        urutan hari pasti dimulai dari ke 1 tidak mungkin dari hari ke 0
    date.append(x+1)
    # menambahkan jumlah kasus positif yang ada pada data ke dalam variable jum_positif
    jum_positif.append(data['jumlah_positif']['value'])
    # menambahkan jumlah kasus menninggal yang ada pada data ke dalam variable jum_meninggal
    jum_meninggoy.append(data['jumlah_meninggal']['value'])
    # menambahkan jumlah kasus menninggal yang ada pada data ke dalam variable jum_sembuh
    jum_sembuh.append(data['jumlah_sembuh']['value'])
    # menambahkan jumlah kasus dirawat yang ada pada data ke dalam variable jum_dirawat
    jum_dirawat.append(data['jumlah_dirawat']['value'])

# membagi plot kedalam 4 baris dan 1 kolom
# mengisi plot pertama
plt.subplot(411)
# memberi judul
plt.title("Data COVID-19 Harian")
# menggambar plot untuk data jumlah kasus positif serta memberi warna merah
plt.plot(date, jum_positif, 'red')
# memberikan keterangan apa data yang ada pada plot tsb
plt.legend(['Jumlah Kasus Positif'])
# mengisi plot kedua
plt.subplot(412)
# menggambar plot untuk data jumlah kasus meninggal serta memberi warna hitam
plt.plot(date, jum_meninggoy, 'black')
# memberikan keterangan apa data yang ada pada plot tsb
plt.legend(['Jumlah Orang yang Meninggoy'])
# mengisi plot ketiga
plt.subplot(413)
# menggambar plot untuk data jumlah kasus sembuh serta memberi warna hijau
plt.plot(date, jum_sembuh, 'green')
# memberikan keterangan apa data yang ada pada plot tsb
plt.legend(['Jumlah Orang yang Sembuh'])
# memberikan keterangan data berdasarkan sumbu-y
plt.ylabel("Jumlah kasus")
# mengisi plot terakhir
plt.subplot(414)
# menggambar plot untuk data jumlah kasus dirawat serta memberi warna oren
plt.plot(date, jum_dirawat, 'orange')
# memberikan keterangan apa data yang ada pada plot tsb
plt.legend(['Jumlah Orang yang Sembuh'])
# memberikan keterangan data berdasarkan sumbu-x
plt.xlabel("Day")
# menampilkan plot
plt.show()
