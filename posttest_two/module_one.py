import math
choice = "0"

def choices():
  print("""
KONVERSI SUHU
Pilih konversi di bawah ini:
1. Fahrenheit ke Celsius
2. Kelvin ke Celsius
3. Reamur ke Celsius
4. Keluar
  """)
  choice = input("Pilih Konversi : ")
  return choice

while choice != "4":
  choice = choices()
  if choice == "1":
    fahrenheit = float(input("Masukkan Nilai Fahrenheit : "))
    celcius = math.floor(fahrenheit - 32 / 1.8)
    print(f"Hasil : {fahrenheit} F > {celcius} C")

  elif choice == "2":

    kelvin = float(input("Masukkan Nilai Kelvin : "))
    celcius = math.floor(kelvin - 273.15)
    print(f"Hasil : {kelvin} K > {celcius} C")

  elif choice == "3":

    reamur = float(input("Masukkan Nilai Reamur : "))
    celcius = math.floor(reamur / 0.8)
    print(f"Hasil : {reamur} R > {celcius} C")

  choice = choices()

print("Terima kasih!")
   
  
  
