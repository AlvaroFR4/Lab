price = input("Enter the price in euros (example: 19.95): ")

parts = price.split(".")

euros = parts[0]
cents = parts[1]

print(f"Euros: {euros}")
print(f"Cents: {cents}")