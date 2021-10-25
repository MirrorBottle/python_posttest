"""
1. Buatlah perintah di python untuk menampilkan Nama, NIM, dan Kelas dengan 1 perintah output dalam 3 baris.
contoh output :
Nama : Udin
NIM : 2109106161
Kelas: Informatika C 2020
"""

student = {
  "name": "Bayu Setiawan",
  "nim": "2109106161",
  "class": "Informatika A 2021",
}

def print_data():
  print(f"""
DATA MAHASISWA
Nama: {student["name"]}
NIM: {student["nim"]}
Kelas: {student["class"]}
  """)

print_data()