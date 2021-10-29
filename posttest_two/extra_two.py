"""
2. Buatlah variabel untuk menampung minimal 5 objek dengan minimal 3 jenis tipe data. Tampilkan nilai dalam per index, bukan dalam satu baris.
"""

students = [
  {"name": "Bayu Setiawan", "age": 18, "gender": "L", "ipk": 3.3},
  {"name": "Shyna", "age": 17, "gender": "P", "ipk": 3.7},
  {"name": "Hya", "age": 17, "gender": "P", "ipk": 3.6},
  {"name": "Mika", "age": 16, "gender": "L", "ipk": 3.7},
  {"name": "Lila", "age": 18, "gender": "P", "ipk": 3.4},
]

print ("DATA MAHASISWA")
for student in students:
  print(f"""
Nama: {student["name"]}
Umur: {student["age"]}
Kelamin: {student["gender"]}
IPK: {student["ipk"]}
  """)