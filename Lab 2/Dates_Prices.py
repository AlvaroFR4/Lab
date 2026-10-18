date_input = input("Date: ")

d, m, y = date_input.split("/")
print(f"Date: {d.zfill(2)}/{m.zfill(2)}/{y}")

product = input("Product: ")
unit_price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

euros = int(unit_price)
cents = int((unit_price - euros) * 100)

print(f"Euros: {euros} Cents: {cents}")

total = unit_price * quantity

print(f"{product} {unit_price:06.2f} {quantity:03d} {total:08.2f}")