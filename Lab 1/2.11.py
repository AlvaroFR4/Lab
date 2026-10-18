product = input("Enter the product name: ")
price = float(input("Enter the price per unit: "))
quantity = int(input("Enter the quantity: "))

total_price = price * quantity

print(f"Product: {product}")
print(f"Price: {price:09.2f} €")
print(f"Quantity: {quantity:03d}")
print(f"Total: {total_price:011.2f} €")