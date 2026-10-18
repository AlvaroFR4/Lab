INTEREST_RATE = 1.04

deposit = float(input("Enter initial deposit amount: "))

year1 = deposit * INTEREST_RATE
year2 = year1 * INTEREST_RATE
year3 = year2 * INTEREST_RATE

print(f"Balance after year 1: {year1:.2f}€")
print(f"Balance after year 2: {year2:.2f}€")
print(f"Balance after year 3: {year3:.2f}€")
