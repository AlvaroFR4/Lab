date = input("Enter your date of birth: ")

first_slash = date.find("/")
second_slash = date.find("/", first_slash + 1)

day = date[0:first_slash]
month = date[first_slash + 1:second_slash]
year = date[second_slash + 1:]

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")