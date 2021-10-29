
import datetime

menus = [
  {"id": '1', "name": "Nasi Kucing", "price": 5000, "type": "food"},
  {"id": '2', "name": "Mie Ayam", "price": 8000, "type": "food"},
  {"id": '3', "name": "Mie Kuah", "price": 7000, "type": "drink"},
  {"id": '4', "name": "Es Teh", "price": 3000, "type": "drink"},
  {"id": '5', "name": "Soda Gembira", "price": 6000, "type": "drink"},
  {"id": '6', "name": "One-Shot Espresso", "price": 8000, "type": "drink"},
]

# FUNCTIONS
def format_rupiah(val):
  return f"Rp. {round(val)}"

def print_discount():
  print("""
DAFTAR DISKON
=================
1. Setiap Pembelian 3 Minuman sebesar 10%
2. Setiap Pembelian 2 Makanan sebesar 5%
3. Setiap pembayaran melalui E-money sebesar 5%
4. Saat weekend sebesar 5%
5. Saat weekdays sebesar 10%
  """)

def print_menus():
  print("""
DAFTAR MENU
=================
  """)
  for menu in menus:
    price = format_rupiah(menu['price'])
    print(f"[{menu['id']}] {menu['name']} ({price})")


# MAIN
print_discount()
print_menus()

is_buying = True
carts = []
while is_buying:
  item_id = input('Apa yang ingin anda beli? ')

  # GET SELECTED ITEM
  item = next((sub for sub in menus if sub['id'] == item_id), None)

  if item == None:
    print('Menu tidak ada')
  else:
    total = input(f"{item['name']}, oke? Berapa banyak? ")
    item['total'] = int(total)
    item['payment'] = item['total'] * item['price']
    carts.append(item)
    print(f"{item['name']} {item['total']} sudah kami catat!")
  is_buying = input('Apa anda ingin memesan lagi? (y/n) ') == 'y'


# COUNT TOTAL CARTS
if len(carts) == 0:
  print("Anda tidak memesan apa-apa.")
else:
  # GET TOTAL FOOD AND DRINKS
  total_food = 0
  total_drinks = 0
  for cart in carts:
    if cart['type'] == 'food':
      total_food += cart['total']
    else:
      total_drinks += cart['total']
  
  # SHOW CART
  print("""
DAFTAR BELANJAAN
=================
  """)
  for cart in carts:
    price = format_rupiah(cart['price'])
    print(f"[{cart['id']}] {cart['name']} x {cart['total']} = {format_rupiah(cart['payment'])}")
  # GET PAYMENT
  print("\n=================")
  
  payment_method = input("Apa anda ingin membayar dengan E-money? (y/n) ")
  payment_discount = 5 if payment_method == "y" else 0

  # GET DAYS DISCOUNT
  day_discount = 10 if datetime.datetime.today().weekday() < 5 else 5

  # GET FOOD AND DRINK DISCOUNT
  food_discount = 10 if total_food >= 3 else 0
  drink_discount = 5 if total_drinks >= 2 else 0

  total_discount = payment_discount + day_discount + food_discount + drink_discount
  total_payment = sum(cart['payment'] for cart in carts)
  cut_discount = total_payment * total_discount / 100
  final_payment = total_payment - cut_discount

  print(f"Total pembelian anda adalah: {format_rupiah(total_payment)}")
  print(f"Anda mendapatkan diskon {total_discount}% senilai {format_rupiah(cut_discount)}")
  print(f"Total pembayaran anda adalah: {format_rupiah(final_payment)}")
  



