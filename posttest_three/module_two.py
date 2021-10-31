from random import randint
import getpass
users = [
  {"id": randint(1, 999), "name": "hiroto", "password": "mypass"},
]

def print_menu():
  print("""
SELAMAT DATANG
=================
1. Buat Akun
2. Login
3. Keluar
  """)

is_running = True


attempts = 1
while is_running:
  print_menu()
  chose = input("Apa yang ingin anda lakukan? ")
  if chose == "1":
    user = {}
    user['id'] = randint(0, 999)
    user['name'] = input("Masukkan nama anda : ")
    user['password'] = getpass.getpass(prompt='Masukkan password : ')
    users.append(user)
    print("Anda berhasil mendaftar! Silahkan login")
  elif chose == "2":
    curr_user = False
    while curr_user == False and attempts <= 3:
      name = input("Masukkan nama anda : ")
      password  = getpass.getpass(prompt='Masukkan password : ')
      curr_user = next((user for user in users if user['name'] == name and user['password'] == password), False)
      if curr_user:
        print(f"Anda berhasil login sebagai {name}")
      else:
        print("Nama atau password salah!")
        attempts += 1
    if attempts >= 3:
      print("Anda sudah tidak bisa login lagi!")
      exit()
  else:
    print("Terima kasih")
    exit()
    



