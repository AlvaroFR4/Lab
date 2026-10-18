phone = input("Enter phone number (+prefix-number-extension): ")

parts = phone.split("-")
main_number = parts[1]

print(f"Main number: {main_number}")