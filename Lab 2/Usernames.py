fullname = input("Full name: ")

no_extra_spaces_name = fullname.strip()

upper_name = no_extra_spaces_name.upper()
letter_count = len(no_extra_spaces_name.replace(" ", ""))

parts = no_extra_spaces_name.split()
username = (parts[0][0] + parts[1]).lower()

print(f"{upper_name} has {letter_count} letters")
print(f"Username: {username}")